# tag: fourteam-bos-utilits-beditor
import curses
import os
import sys
import re
from datetime import datetime

class BaboEditor:
    def __init__(self, stdscr, filename=None):
        self.stdscr = stdscr
        self.filename = filename
        self.lines = []
        self.current_line = 0
        self.current_pos = 0
        self.offset = 0
        self.message = ""
        self.modified = False
        self.quit_confirmation = False
        self.search_term = ""
        self.replace_term = ""
        self.search_direction = 1
        self.mark_start = None
        self.mark_end = None
        self.clipboard = []
        self.undo_stack = []
        self.redo_stack = []
        self.backup_extension = ".save"
        
        if filename and os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                self.lines = content.split('\n')
                if content and content[-1] == '\n':
                    self.lines.append("")
        else:
            self.lines = [""]
        
        self.save_state()
        curses.use_default_colors()
        curses.curs_set(1)
    
    def save_state(self):
        if len(self.undo_stack) > 100:
            self.undo_stack.pop(0)
        self.undo_stack.append({
            'lines': self.lines.copy(),
            'current_line': self.current_line,
            'current_pos': self.current_pos
        })
        self.redo_stack.clear()
    
    def undo(self):
        if len(self.undo_stack) > 1:
            self.redo_stack.append(self.undo_stack.pop())
            state = self.undo_stack[-1]
            self.lines = state['lines'].copy()
            self.current_line = state['current_line']
            self.current_pos = state['current_pos']
            self.modified = True
            return True
        return False
    
    def redo(self):
        if self.redo_stack:
            state = self.redo_stack.pop()
            self.undo_stack.append(state)
            self.lines = state['lines'].copy()
            self.current_line = state['current_line']
            self.current_pos = state['current_pos']
            self.modified = True
            return True
        return False
    
    def display(self):
        self.stdscr.clear()
        height, width = self.stdscr.getmaxyx()
        
        status = f" bEditor - {self.filename or '[New File]'}"
        if self.modified:
            status += "*"
        self.stdscr.addstr(0, 0, status.ljust(width)[:width-1], curses.A_REVERSE)
        
        edit_height = height - 3
        for i in range(edit_height):
            line_idx = i + self.offset
            if line_idx < len(self.lines):
                line = self.lines[line_idx]
                if line_idx == self.current_line:
                    attr = curses.A_BOLD
                else:
                    attr = curses.A_NORMAL
                
                if self.mark_start and self.mark_end:
                    start_line, start_pos = self.mark_start
                    end_line, end_pos = self.mark_end
                    if (start_line <= line_idx <= end_line and 
                        (line_idx > start_line or start_pos <= len(line)) and
                        (line_idx < end_line or end_pos >= 0)):
                        attr |= curses.A_REVERSE
                
                line_num = f"{line_idx + 1:3d} "
                self.stdscr.addstr(i + 1, 0, line_num, curses.A_DIM)
                
                display_line = line.replace('\t', '    ')
                if len(display_line) > width - 5:
                    display_line = display_line[:width - 8] + "..."
                try:
                    self.stdscr.addstr(i + 1, 4, display_line, attr)
                except curses.error:
                    pass
        
        now = datetime.now().strftime("%H:%M:%S")
        pos_info = f"Line {self.current_line + 1}/{len(self.lines)}, Col {self.current_pos + 1}"
        help_text = "^G Help ^O Save ^W Find ^K Cut ^U Paste ^T Replace ^C Position ^M Mark"
        
        status_line = f" {pos_info} | {now} | {help_text}"
        self.stdscr.addstr(height - 2, 0, status_line.ljust(width)[:width-1], curses.A_REVERSE)
        
        if self.message:
            self.stdscr.addstr(height - 1, 0, self.message[:width-1])
            self.message = ""
        
        try:
            cursor_y = self.current_line - self.offset + 1
            if 1 <= cursor_y < height - 2:
                cursor_x = min(self.current_pos + 4, width - 1)
                self.stdscr.move(cursor_y, cursor_x)
        except curses.error:
            pass
        
        self.stdscr.refresh()
    
    def show_help(self):
        height, width = self.stdscr.getmaxyx()
        help_lines = [
            "bEditor help",
            "=" * 50,
            "File:",
            "Ctrl+O - Save",
            "Ctrl+R - Insert File",
            "Ctrl+S - Save As",
            "Ctrl+X - Exit",
            "",
            "Edit:",
            "Ctrl+K - Cut line/block",
            "Ctrl+U - Paste",
            "Ctrl+6 - Copy",
            "Ctrl+W - Find",
            "Ctrl+\\ - Replace",
            "Ctrl+T - Spell check",
            "Ctrl+M - Toggle mark",
            "",
            "Navigation:",
            "Ctrl+C - Show position",
            "Ctrl+_ - Go to line",
            "Ctrl+A - Beginning of line",
            "Ctrl+E - End of line",
            "Ctrl+Y - Page up",
            "Ctrl+V - Page down",
            "",
            "Additional:",
            "Ctrl+G - This help",
            "Ctrl+Z - Undo",
            "Ctrl+Y - Redo",
            "Ctrl+D - Delete character",
            "Ctrl+H - Backspace",
            "Ctrl+F - Forward",
            "Ctrl+B - Backward",
            "",
            "Press any key to continue..."
        ]
        
        help_height = min(len(help_lines) + 2, height - 4)
        help_width = min(max(len(line) for line in help_lines) + 4, width - 4)
        start_y = (height - help_height) // 2
        start_x = (width - help_width) // 2
        
        help_win = curses.newwin(help_height, help_width, start_y, start_x)
        help_win.border()
        help_win.bkgd(' ', curses.A_REVERSE)
        
        help_win.addstr(0, 2, " Babo Help ", curses.A_BOLD | curses.A_REVERSE)
        
        for i, line in enumerate(help_lines):
            if i < help_height - 2:
                help_win.addstr(i + 1, 2, line[:help_width-3])
        
        help_win.refresh()
        self.stdscr.getch()
    
    def save_file(self, filename=None):
        if filename:
            self.filename = filename
        
        if not self.filename:
            return self.prompt_save_as()
        
        try:
            backup_file = self.filename + self.backup_extension
            if os.path.exists(self.filename):
                os.rename(self.filename, backup_file)
            
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write('\n'.join(self.lines))
            self.modified = False
            self.message = f"File saved: {self.filename}"
            if os.path.exists(backup_file):
                os.remove(backup_file)
            return True
        except Exception as e:
            self.message = f"Save error: {str(e)}"
            return False
    
    def prompt_save_as(self):
        height, width = self.stdscr.getmaxyx()
        prompt = "File name to save: "
        
        input_win = curses.newwin(3, width - 4, height - 4, 2)
        input_win.border()
        input_win.addstr(0, 2, " Save As ", curses.A_BOLD)
        input_win.addstr(1, 2, prompt)
        
        input_win.refresh()
        
        curses.echo()
        filename = input_win.getstr(1, len(prompt) + 2, width - len(prompt) - 10).decode('utf-8')
        curses.noecho()
        
        if filename:
            return self.save_file(filename)
        return False
    
    def insert_file(self):
        height, width = self.stdscr.getmaxyx()
        prompt = "Insert file: "
        
        input_win = curses.newwin(3, width - 4, height - 4, 2)
        input_win.border()
        input_win.addstr(0, 2, " Insert File ", curses.A_BOLD)
        input_win.addstr(1, 2, prompt)
        
        input_win.refresh()
        
        curses.echo()
        filename = input_win.getstr(1, len(prompt) + 2, width - len(prompt) - 10).decode('utf-8')
        curses.noecho()
        
        if filename and os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                    insert_lines = content.split('\n')
                
                self.save_state()
                current_text = self.lines[self.current_line]
                before_cursor = current_text[:self.current_pos]
                after_cursor = current_text[self.current_pos:]
                
                new_lines = self.lines[:self.current_line]
                if insert_lines:
                    new_lines.append(before_cursor + insert_lines[0])
                    new_lines.extend(insert_lines[1:])
                    new_lines[-1] += after_cursor
                else:
                    new_lines.append(before_cursor + after_cursor)
                
                new_lines.extend(self.lines[self.current_line + 1:])
                self.lines = new_lines
                self.modified = True
                self.message = f"File inserted: {filename}"
            except Exception as e:
                self.message = f"Insert error: {str(e)}"
        elif filename:
            self.message = f"File not found: {filename}"
    
    def find_text(self, replace_mode=False):
        height, width = self.stdscr.getmaxyx()
        prompt = "Replace: " if replace_mode else "Find: "
        
        input_win = curses.newwin(3, width - 4, height - 4, 2)
        input_win.border()
        title = " Replace " if replace_mode else " Find "
        input_win.addstr(0, 2, title, curses.A_BOLD)
        input_win.addstr(1, 2, prompt)
        
        input_win.refresh()
        
        curses.echo()
        if replace_mode and self.search_term:
            input_win.addstr(1, len(prompt) + 2, self.search_term)
        term = input_win.getstr(1, len(prompt) + 2, width - len(prompt) - 10).decode('utf-8')
        curses.noecho()
        
        if term:
            self.search_term = term
            if replace_mode:
                replace_prompt = "Replace with: "
                input_win.addstr(1, 2, " " * width)
                input_win.addstr(1, 2, replace_prompt)
                input_win.refresh()
                curses.echo()
                if self.replace_term:
                    input_win.addstr(1, len(replace_prompt) + 2, self.replace_term)
                replace_term = input_win.getstr(1, len(replace_prompt) + 2, width - len(replace_prompt) - 10).decode('utf-8')
                curses.noecho()
                self.replace_term = replace_term
                return self.replace_next()
            else:
                return self.find_next()
        return False
    
    def find_next(self, backward=False):
        if not self.search_term:
            return self.find_text()
        
        start_line = self.current_line
        start_pos = self.current_pos + (0 if backward else 1)
        
        lines_to_search = list(range(len(self.lines)))
        if backward:
            lines_to_search = list(reversed(lines_to_search))
        
        for i in lines_to_search:
            line = self.lines[i]
            if i == start_line:
                if backward:
                    pos = line.rfind(self.search_term, 0, start_pos)
                else:
                    pos = line.find(self.search_term, start_pos)
            else:
                if backward:
                    pos = line.rfind(self.search_term)
                else:
                    pos = line.find(self.search_term)
            
            if pos != -1:
                self.current_line = i
                self.current_pos = pos
                height = self.stdscr.getmaxyx()[0]
                self.offset = max(0, i - height // 2)
                self.message = f"Found: {self.search_term}"
                return True
        
        self.message = f"Text not found: {self.search_term}"
        return False
    
    def replace_next(self):
        if not self.search_term:
            return self.find_text(True)
        
        if self.find_next():
            self.save_state()
            line = self.lines[self.current_line]
            new_line = line[:self.current_pos] + self.replace_term + line[self.current_pos + len(self.search_term):]
            self.lines[self.current_line] = new_line
            self.current_pos += len(self.replace_term)
            self.modified = True
            self.message = f"Replaced: {self.search_term} -> {self.replace_term}"
            return True
        return False
    
    def replace_all(self):
        if not self.search_term:
            return self.find_text(True)
        
        count = 0
        self.save_state()
        for i in range(len(self.lines)):
            line = self.lines[i]
            if self.search_term in line:
                new_line = line.replace(self.search_term, self.replace_term)
                self.lines[i] = new_line
                count += line.count(self.search_term)
        
        if count > 0:
            self.modified = True
            self.message = f"Replaced {count} occurrences"
        else:
            self.message = "No occurrences found"
    
    def cut_line(self):
        self.save_state()
        if self.mark_start and self.mark_end:
            start_line, start_pos = self.mark_start
            end_line, end_pos = self.mark_end
            
            if start_line == end_line:
                cut_text = self.lines[start_line][start_pos:end_pos]
                self.lines[start_line] = self.lines[start_line][:start_pos] + self.lines[start_line][end_pos:]
                self.clipboard = [cut_text]
            else:
                cut_lines = []
                first_line = self.lines[start_line][start_pos:]
                cut_lines.append(first_line)
                
                for i in range(start_line + 1, end_line):
                    cut_lines.append(self.lines[i])
                
                last_line = self.lines[end_line][:end_pos]
                cut_lines.append(last_line)
                self.clipboard = cut_lines
                
                self.lines[start_line] = self.lines[start_line][:start_pos] + self.lines[end_line][end_pos:]
                del self.lines[start_line + 1:end_line + 1]
            
            self.mark_start = None
            self.mark_end = None
        else:
            self.clipboard = [self.lines[self.current_line]]
            del self.lines[self.current_line]
            if not self.lines:
                self.lines = [""]
            if self.current_line >= len(self.lines):
                self.current_line = len(self.lines) - 1
        
        self.modified = True
        self.message = "Text cut"
    
    def copy_text(self):
        if self.mark_start and self.mark_end:
            start_line, start_pos = self.mark_start
            end_line, end_pos = self.mark_end
            
            if start_line == end_line:
                self.clipboard = [self.lines[start_line][start_pos:end_pos]]
            else:
                copy_lines = []
                copy_lines.append(self.lines[start_line][start_pos:])
                for i in range(start_line + 1, end_line):
                    copy_lines.append(self.lines[i])
                copy_lines.append(self.lines[end_line][:end_pos])
                self.clipboard = copy_lines
            self.message = "Text copied"
        else:
            self.clipboard = [self.lines[self.current_line]]
            self.message = "Line copied"
    
    def paste_text(self):
        if not self.clipboard:
            return
        
        self.save_state()
        current_line = self.lines[self.current_line]
        before_cursor = current_line[:self.current_pos]
        after_cursor = current_line[self.current_pos:]
        
        if len(self.clipboard) == 1:
            new_line = before_cursor + self.clipboard[0] + after_cursor
            self.lines[self.current_line] = new_line
            self.current_pos += len(self.clipboard[0])
        else:
            new_lines = self.lines[:self.current_line]
            new_lines.append(before_cursor + self.clipboard[0])
            new_lines.extend(self.clipboard[1:-1])
            new_lines.append(self.clipboard[-1] + after_cursor)
            new_lines.extend(self.lines[self.current_line + 1:])
            self.lines = new_lines
        
        self.modified = True
        self.message = "Text pasted"
    
    def toggle_mark(self):
        if self.mark_start is None:
            self.mark_start = (self.current_line, self.current_pos)
            self.message = "Mark set"
        else:
            self.mark_end = (self.current_line, self.current_pos)
            if self.mark_start > self.mark_end:
                self.mark_start, self.mark_end = self.mark_end, self.mark_start
            self.message = "Block selected"
    
    def clear_mark(self):
        self.mark_start = None
        self.mark_end = None
        self.message = "Marks cleared"
    
    def goto_line(self):
        height, width = self.stdscr.getmaxyx()
        prompt = "Go to line: "
        
        input_win = curses.newwin(3, width - 4, height - 4, 2)
        input_win.border()
        input_win.addstr(0, 2, " Go To Line ", curses.A_BOLD)
        input_win.addstr(1, 2, prompt)
        
        input_win.refresh()
        
        curses.echo()
        line_input = input_win.getstr(1, len(prompt) + 2, 10).decode('utf-8')
        curses.noecho()
        
        if line_input and line_input.isdigit():
            line_num = int(line_input) - 1
            if 0 <= line_num < len(self.lines):
                self.current_line = line_num
                self.current_pos = 0
                height = self.stdscr.getmaxyx()[0]
                self.offset = max(0, line_num - height // 2)
                self.message = f"Go to line {line_num + 1}"
            else:
                self.message = "Invalid line number"
    
    def justify_paragraph(self):
        self.save_state()
        if self.mark_start and self.mark_end:
            start_line, _ = self.mark_start
            end_line, _ = self.mark_end
        else:
            start_line = self.current_line
            end_line = self.current_line
        
        paragraph = []
        for i in range(start_line, end_line + 1):
            if i < len(self.lines):
                paragraph.append(self.lines[i].strip())
        
        justified = ' '.join(paragraph)
        width = 80
        
        words = justified.split()
        lines = []
        current_line = []
        current_length = 0
        
        for word in words:
            if current_length + len(word) + len(current_line) <= width:
                current_line.append(word)
                current_length += len(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        self.lines[start_line:end_line + 1] = lines
        self.modified = True
        self.message = "Paragraph justified"
    
    def show_position(self):
        total_chars = sum(len(line) for line in self.lines)
        self.message = f"Line {self.current_line + 1}/{len(self.lines)}, Col {self.current_pos + 1}, Total chars: {total_chars}"
    
    def spell_check(self):
        self.message = "Spell check (stub)"
    
    def handle_input(self, key):
        current_line_text = self.lines[self.current_line]
        
        
        if key in [10, 13, curses.KEY_ENTER, 459, 546]:
            left_part = current_line_text[:self.current_pos]
            right_part = current_line_text[self.current_pos:]
            self.save_state()
            self.lines[self.current_line] = left_part
            self.lines.insert(self.current_line + 1, right_part)
            self.current_line += 1
            self.current_pos = 0
            self.modified = True
            return
            
        if key == curses.KEY_UP:
            if self.current_line > 0:
                self.current_line -= 1
                self.current_pos = min(self.current_pos, len(self.lines[self.current_line]))
                if self.current_line < self.offset:
                    self.offset = self.current_line
                    
        elif key == curses.KEY_DOWN:
            if self.current_line < len(self.lines) - 1:
                self.current_line += 1
                self.current_pos = min(self.current_pos, len(self.lines[self.current_line]))
                height = self.stdscr.getmaxyx()[0]
                if self.current_line >= self.offset + height - 3:
                    self.offset = self.current_line - height + 4
                    
        elif key == curses.KEY_LEFT:
            if self.current_pos > 0:
                self.current_pos -= 1
            elif self.current_line > 0:
                self.current_line -= 1
                self.current_pos = len(self.lines[self.current_line])
                
        elif key == curses.KEY_RIGHT:
            if self.current_pos < len(current_line_text):
                self.current_pos += 1
            elif self.current_line < len(self.lines) - 1:
                self.current_line += 1
                self.current_pos = 0
                
        elif key == curses.KEY_HOME:
            self.current_pos = 0
            
        elif key == curses.KEY_END:
            self.current_pos = len(current_line_text)
            
        elif key == curses.KEY_PPAGE:
            height = self.stdscr.getmaxyx()[0]
            self.current_line = max(0, self.current_line - (height - 3))
            self.offset = max(0, self.offset - (height - 3))
            self.current_pos = min(self.current_pos, len(self.lines[self.current_line]))
            
        elif key == curses.KEY_NPAGE:
            height = self.stdscr.getmaxyx()[0]
            self.current_line = min(len(self.lines) - 1, self.current_line + (height - 3))
            self.offset = min(len(self.lines) - 1, self.offset + (height - 3))
            self.current_pos = min(self.current_pos, len(self.lines[self.current_line]))
            
        elif key == curses.KEY_BACKSPACE or key == 127 or key == 8:
            self.save_state()
            if self.current_pos > 0:
                self.lines[self.current_line] = (current_line_text[:self.current_pos-1] + 
                                               current_line_text[self.current_pos:])
                self.current_pos -= 1
                self.modified = True
            elif self.current_line > 0:
                prev_line = self.lines[self.current_line - 1]
                new_pos = len(prev_line)
                self.lines[self.current_line - 1] = prev_line + current_line_text
                del self.lines[self.current_line]
                self.current_line -= 1
                self.current_pos = new_pos
                self.modified = True
                
        elif key == curses.KEY_DC or key == 4:
            self.save_state()
            if self.current_pos < len(current_line_text):
                self.lines[self.current_line] = (current_line_text[:self.current_pos] + 
                                               current_line_text[self.current_pos+1:])
                self.modified = True
            elif self.current_line < len(self.lines) - 1:
                self.lines[self.current_line] = current_line_text + self.lines[self.current_line + 1]
                del self.lines[self.current_line + 1]
                self.modified = True
                
        elif 32 <= key <= 126:
            char = chr(key)
            self.save_state()
            self.lines[self.current_line] = (current_line_text[:self.current_pos] + char + 
                                           current_line_text[self.current_pos:])
            self.current_pos += 1
            self.modified = True
            
        elif key == 9:
            tab_spaces = "    "
            self.save_state()
            self.lines[self.current_line] = (current_line_text[:self.current_pos] + tab_spaces + 
                                           current_line_text[self.current_pos:])
            self.current_pos += len(tab_spaces)
            self.modified = True
    
    def run(self):
        while True:
            self.display()
            key = self.stdscr.getch()
            
            if key == 7:  # Ctrl+G
                self.show_help()
            elif key == 19:  # Ctrl+S
                self.save_file()
            elif key == 15:  # Ctrl+O
                self.prompt_save_as()
            elif key == 24:  # Ctrl+X
                if self.modified and not self.quit_confirmation:
                    self.message = "File modified! Press Ctrl+X again to exit without saving or Ctrl+S to save"
                    self.quit_confirmation = True
                else:
                    if self.modified:
                        self.message = "Exit without saving"
                    return
            elif key == 23:  # Ctrl+W
                self.find_text()
            elif key == 6:  # Ctrl+F
                self.find_next()
            elif key == 2:  # Ctrl+B
                self.find_next(backward=True)
            elif key == 18:  # Ctrl+R
                self.insert_file()
            elif key == 11:  # Ctrl+K
                self.cut_line()
            elif key == 21:  # Ctrl+U
                self.paste_text()
            elif key == 30:  # Ctrl+6 (^)
                self.copy_text()
            elif key == 28:  # Ctrl+\
                self.toggle_mark()
            elif key == 3:  # Ctrl+C
                self.show_position()
            elif key == 31:  # Ctrl+_
                self.goto_line()
            elif key == 20:  # Ctrl+T
                self.spell_check()
            elif key == 26:  # Ctrl+Z
                if self.undo():
                    self.message = "Undone"
                else:
                    self.message = "Nothing to undo"
            elif key == 25:  # Ctrl+Y
                if self.redo():
                    self.message = "Redone"
                else:
                    self.message = "Nothing to redo"
            elif key == 27:  # Esc
                self.clear_mark()
            elif key == 12:  # Ctrl+L
                self.replace_next()
            elif key == 4:  # Ctrl+D
                self.handle_input(curses.KEY_DC)
            elif key == 8:  # Ctrl+H
                self.handle_input(curses.KEY_BACKSPACE)
            else:
                self.quit_confirmation = False
                self.handle_input(key)

def main(stdscr, filename=None):
    # Включаем обработку специальных клавиш
    stdscr.keypad(True)
    
    editor = BaboEditor(stdscr, filename)
    editor.run()

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else None
    
    # Установка windows-curses если нужно
    try:
        import curses
    except ImportError:
        print("Curses not available. Installing windows-curses...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "windows-curses"])
        import curses
    
    try:
        curses.wrapper(main, filename)
    except KeyboardInterrupt:
        print("\nExit from Babo")
