def hitung_luas(X,Y,Z):
    L = 2 * X + Y * Z
    return L

print("<!DOCTYPE html>\n")
print("""<html>
    <head>
	<title> Kegiatan 3 </title>
    </head>
    <body>
	<table border="0">
	    <tr>
		<td colspan="4"><p align="center"><b> Bangun Geometri </b></p></td>
	    </tr>
	    <tr>
		<td> Nama Bangun </td>
		<td> : </td>
		<td> Prisma </td>
	    </tr>
	    <tr>
		<td> Dimensi (2D/3D) </td>
		<td> : </td>
		<td> 3D </td>
	    </tr>
	    <tr>
		<td> Rumus Luas </td>
		<td> : </td>
		<td> 2 × Luas alas + Keliling alas × Tinggi Prisma </td>
	    </tr>
	    <tr>
		<td> Luas Alas </td>
		<td> : </td>
		<td> 24 </td>
            </tr>
            <tr>
		<td> Keliling Alas </td>
		<td> : </td>
		<td> 24 </td>
            </tr>
            <tr>
		<td> Tinggi Prisma </td>
		<td> : </td>
		<td> 5 </td>
            </tr>
            <tr>
		<td> Luas </td>
		<td> : </td>""")
print("                <td>", hitung_luas(24,24,5),"<td")
print("""       </table>
    </body>
</html>""")


    

