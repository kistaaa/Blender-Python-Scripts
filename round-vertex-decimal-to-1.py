# round all vertex from the active mesh to 1 decimal positions

import bpy
import bmesh

# Get the active mesh
me = bpy.context.object.data

# Get a BMesh representation
bm = bmesh.new()   # create an empty BMesh
bm.from_mesh(me)   # fill it in from a Mesh


# find vertices and round their xyz to 1 decimal
for v in bm.verts:
    v.co.x = round(v.co.x, 1)
    v.co.y = round(v.co.y, 1)
    v.co.z = round(v.co.z, 1)

# Finish up, write the bmesh back to the mesh
bm.to_mesh(me)
bm.free()  # free and prevent further access