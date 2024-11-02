# ctx.py
# Basic library for library for coloring text in the command line.
# v. 1.0, 2024 (C) DAREKPAGES
# Python 3.11.10
#
# Use: 
# print(ctx.ft_bold_white + ctx.bg_blue, ' TEST ', ctx.clr)
#

# Font style:
ft_faint_white= '\033[2;37m'
ft_faint_black= '\033[2;30m'
ft_faint_yellow= '\033[2;33m'
ft_faint_red= '\033[2;31m'
ft_faint_magenta= '\033[2;35m'
ft_faint_cyan= '\033[2;36m'
ft_faint_blue= '\033[2;34m'
ft_faint_green= '\033[2;32m'

ft_white= '\033[37m'
ft_black= '\033[30m'
ft_yellow= '\033[33m'
ft_red= '\033[31m'
ft_magenta= '\033[35m'
ft_cyan= '\033[36m'
ft_blue= '\033[34m'
ft_green= '\033[32m'

ft_italic_white= '\033[3;37m'
ft_italic_black= '\033[3;30m'
ft_italic_yellow= '\033[3;33m'
ft_italic_red= '\033[3;31m'
ft_italic_magenta= '\033[3;35m'
ft_italic_cyan= '\033[3;36m'
ft_italic_blue= '\033[3;34m'
ft_italic_green= '\033[3;32m'

ft_bold_white= '\033[1;37m'
ft_bold_black= '\033[1;30m'
ft_bold_yellow= '\033[1;33m'
ft_bold_red= '\033[1;31m'
ft_bold_magenta= '\033[1;35m'
ft_bold_cyan= '\033[1;36m'
ft_bold_blue= '\033[1;34m'
ft_bold_green= '\033[1;32m'

# Background style:
bg_white = '\033[107m'
bg_grey = '\033[100m'
bg_black = '\033[40m'
bg_yellow = '\033[43m'
bg_red = '\033[41m'
bg_magenta = '\033[45m'
bg_cyan = '\033[46m'
bg_blue = '\033[44m'
bg_green = '\033[42m'

# Reset all style:
clr = '\033[0m'
