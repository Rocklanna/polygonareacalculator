class Rectangle:

    def __init__(self,width,height):
        self.name="Rectangle";
        self.width=width;
        self.height=height;
    
    def __str__(self):
      output=self.name +"(width="+str(self.width) +", "+"height="+str(self.height)+")";

      return output;

    def set_width(self,width):
       self.width=width;
    
    def set_height(self,height):
       self.height=height;
    
    def get_area(self):
      return self.height*self.width;
    
    def get_perimeter(self):
      return (2*self.height)+(2*self.width);
    
    def get_diagonal(self):
      return ((self.height ** 2)+(self.width ** 2)) ** .5;
    
    def get_picture(self):
        row = self.height;
        column =self.width ;
        output="";
        if row>50 or column>50:
          return "Too big for picture."
        
        while (row>0):
            output += "*" * column;
            output +="\n";
            row-=1;
        
        return output;
    
    def get_amount_inside(self,shape):
      column=self.width//shape.width;
      row=self.height//shape.height;

      return column * row;
    
class Square(Rectangle):
  def __init__(self,side):
    self.name="Square";
    self.width=side;
    self.height=side;

  def __str__(self):
      output=self.name +"(side="+str(self.width)+")"; 
      return output; 

  def set_side(self,side):
    self.width=side;
    self.height=side;  

  def set_width(self,width):
      self.width=width;
      self.height=width; 
    
  def set_height(self,height):
     self.width=height;
     self.height=height;  


