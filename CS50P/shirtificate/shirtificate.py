from fpdf import FPDF
name = input('Name: ')
a = FPDF(orientation="P", unit="mm", format="A4")
a.add_page()
a.set_font('helvetica', 'B', 30)
a.set_text_color(r=0, g=0, b=0)
a.image('shirtificate.png', x= 20, y= 80, w=170)
a.cell(200, 50, 'CS50 Shirtificate', new_x="LMARGIN", new_y="NEXT", align='C')
a.set_text_color(r=255, g=255, b=255)
a.cell(200, 150, f'{name} took CS50', new_x="LMARGIN", new_y="NEXT", align='C')
a.output('shirtificate.pdf')

