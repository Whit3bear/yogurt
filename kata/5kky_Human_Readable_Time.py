def make_readable(seconds):
    return f'{seconds//3600%100:02d}:{seconds//60%60:02d}:{seconds%60:02d}'