buildings = []
skyline_output = []

#reading and inserting buildings points 
while 1:
    line = input()
    caracter = "()"
    for i in range(0,len(caracter)):
        line = line.replace(caracter[i],"")
    value = line.split(",")
    value = ([int(value[0]), int(value[1]), int(value[2])])
    if value[0] == 0 and value[1] == 0 and value[2] == 0:
            break
    buildings.append(eval('value'))
    

begin_building = 0
height_building = 1
end_building = 2
#smallest building begin point  (first building)
left = min(b[begin_building] for b in buildings)
#biggest building end point (last building)
right = max(b[end_building] for b in buildings)
last_height = None

#first building point to last building point
for i in range(left, right + 1):
    heights = [b[height_building] for b in buildings if b[begin_building] <= i < b[end_building]]
    height = max(heights) if heights else 0
    # if the current height is different from the last one
    #then update the skyline_output with the building point and your height
    if height != last_height:
        skyline_output += [i]
        skyline_output += [height]
        last_height = height
result = ','.join(map(str, skyline_output))
print("%s%s%s" % ('(',result,')'))

    


