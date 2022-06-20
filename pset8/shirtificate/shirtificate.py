from fpdf import FPDF

class PDF(FPDF):
  def header(self):
    self.set_auto_page_break(False)
    self.set_font("helvetica", size=30)
    self.cell(w=0, h=50, txt="CS50 shirtificate", align="C", new_x="LMARGIN", new_y="NEXT" )



def main():
  name = input("Name: ")
  pdf = PDF()
  pdf.add_page()
  pdf.image("shirtificate.png", x=15, y=50, w=pdf.epw)
  pdf.set_text_color(255)
  pdf.cell(w=0, h=150, txt=f"{name} took CS50", align="C")

  pdf.output("shirtificate.pdf")

if __name__ == "__main__":
  main()