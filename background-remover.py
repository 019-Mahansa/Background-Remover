from withoutbg import WithoutBG

img = WithoutBG.opensource()
result = img.remove_background("INSERT YOUR IMG NAME IN HERE")
result.save("INSERT YOUR IMG NAME AFTER GETTING BACKGROUND REMOVED")