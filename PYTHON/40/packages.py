import geometrie # 1. import celého package
# from geometrie import circle

print(geometrie.XYZ)
print(geometrie.circle.get_area)

"""
1. import celého package -> ale musím mít v init definované co vše chci mít k dispozici
2. import jednotlivých části package (from geometrie import circle)
- zde není potřeba mít definované v init
"""
