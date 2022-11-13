red = int(input())
blue = int(input())
green = int(input())

sorted = [red, blue, green].sort()

print(red - min(sorted), blue - min(sorted), green - min(sorted))
