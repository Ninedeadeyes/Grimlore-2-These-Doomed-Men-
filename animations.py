from __future__ import annotations
import os
import time

def clear() -> None:
    """Clear the terminal screen using the appropriate OS command."""
    os.system('cls' if os.name == 'nt' else 'clear')

def intro_animation() -> None:
    """Play the intro loading animation."""
    clear()
    loop = 0

    while loop < 1:
        loop += 1

        print("""










                                                                             
           xxxx                                                                 
           xxx                                                                  
           xx                                                      x x x             
           xxx x                                                                
           xx                                                                   
           xx                                                                   
          x   x                                                                 
        x       x                                                               
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

                   """)
        time.sleep(.5)
        clear()

        print(""" 








                                                                            

                                                       
                 xxxx                                                           
                 xxx                                                            
                 xx                                x x x                                                             
                 xxxx                                                           
                 xx                                                             
                 xx                                                             
                 xx                                                             
                x  x                                                            
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                      
 
                   """)
        time.sleep(.5)
        clear()

        print("""  
              








                                                                 
                                                  
                       xxxx                                                     
                       xxx                                                      
                       xx                      x x x                                  
                       xxx x                                                    
                       xx                                                       
                       xx                                                       
                      x   x                                                     
                    x       x                                                   
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

                   """)
        time.sleep(.5)
        clear()

        print("""   
              








                                                        
                                            
                             xxxx                                               
                             xxx                                                
                             xx          x x x                                            
                             xxxx                                               
                             xx                                                 
                             xx                                                 
                             xx                                                 
                            x  x                                                
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

                   """)
        time.sleep(.5)
        clear()

        print("""   
              








                                         
                          
                                   xxxx                                         
                                   xxx                                          
                       x x x       xx                                           
                                   xxx x                                        
                                   xx                                           
                                   xx                                           
                                  x   x                                         
                                x       x                                       
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

                   """)
        time.sleep(.5)
        clear()

        print("""   
              








                             
              
                                         xxxx                                   
                                         xxx                                    
            x x x                        xx                                     
                                         xxxx                                   
                                         xx                                     
                                         xx                                     
                                         xx x x                                   
                                      x x x   x                                
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

                   """)
        time.sleep(.5)
        clear()

        print("""  









                 
              
                                          xxxx                                   
                                          xxx                                    
                                          xx                                     
                                          xxx                                   
                                          xx x                                   
                                          xx                                     
                                         xx                                     
                                      x x x                                   
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

                   """)
        time.sleep(.5)
        clear()

        print("""   









      
              
                                                                         
                                                                             
                                    xx                                       
                                   xxx    xxx                                   
                                  xxxx    xx x                                   
                                          xx                                     
                                         xx                                     
                                      x x x                                   
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

                   """)
        time.sleep(.5)
        clear()

        print("""    
              










                                                               
                                                                             
                                                                            
                                          xxx                                   
                             xxxx         xx x                                   
                             xxx          xx                                     
                             xx          xx                                     
                                      x x x                                   
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

                   """)
        time.sleep(.5)
        clear()

        print("""   










              
                                                                         
                                                                             
                                                                            
                                                                           
                                               x x                           
                           xx                 x x x                                    
                          xxx                x x                                 
                         xxxx           x x x                                
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

                   """)
        time.sleep(.5)
        clear()

        print("""   
              









              
                                                                                 
                                                                             
                                                                            
                                                                           
                                                                            
                    xxxx                                                           
                    xxx                   x x x x x x                                  
                    xx                x x x x x x x x                               
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

                   """)
        time.sleep(.5)
        clear()


        print("""                          
              
                                Grimlore 2 :  These Doomed Men                                               
                                        by Tommy Kwong  


              







                                                                            
                                                                           
                                                                            
                    xxxx                                                           
                    xxx                   x x x x x x                                  
                    xx                x x x x x x x x                               
  dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd

                   """)
        time.sleep(1.0)
        input("Press enter to continue")
        clear()

def loading_animation() -> None:
    """Play the intro loading animation."""
    clear()
    loop = 0

    while loop < 2:
        loop += 1
        clear()
        print("""   
              









                                                                             
                               xx  x                            xxxxx
                               xx   x                           xxxxx  
                               xxxxxxxx                           xx
                               xx   x                         x x xxx  
                               xx  x                              xx x 
                               xx                                 xx  
                              x   x                              x  x  
                            x      x                             x   x
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                       
                      loading . 
                   """)
        time.sleep(.4)
        clear()

        print("""   
              




              




              
                               xx  x                       xxxxx       
                               xx   x          x           xxxxx        
                               xxxxxxxx   xxxxxxx            xx      
                               xx   x          x         x x xxx               
                               xx  x                         xx x   
                               xx                            xx
                              x   x                        x   x
                            x      x                      x     x
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                       
                      loading ..
                   """)
        time.sleep(.4)
        clear()

        print("""    










              
                               xx  x                   xxxxx           
                               xx   x              x   xxxxx           
                               xxxxxxxx       xxxxxxx   xx         
                               xx   x              x  x xxx            
                               xx  x                 x  xx  x  
                               xx                       xx      
                              x   x                    x  x    
                            x      x                    x   x  
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                  
                      loading ... 
                   """)
        time.sleep(.4)
        clear()

        print("""    
              









              
                               xx  x                   xxxxx            
                               xx   x                  xxxxx           
                               xxxxxxxx           xxxxxxxx          
                               xx   x                  xxx           
                               xx  x                    xx      
                               xx                       xx      
                              x   x                    x   x     
                            x      x                  x   x     
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                       
                      loading . 
                   """)
        time.sleep(.4)
        clear()

        print("""   
              









              
                               xx  x                               
                               xx   x              xxxxx           x    
                               xxxxxxxx            xxxxx       xxxxxxx 
                               xx   x                 xx           x   
                               xx  x                x xx       
                               xx                  x  xx        
                              x   x                   xx        
                            x      x                  xxxxx        
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                    
                      loading ..
                   """)
        
        time.sleep(.4)
        clear()
        print("""    





              




              
                               xx  x                               
                               xx   x           xxxxx                    x    
                               xxxxxxxx         xxxxx               xxxxxxx 
                               xx   x              xx                    x   
                               xx  x              x xx       
                               xx                x   xx        
                              x   x                   xx        
                            x      x                   xxxxx        
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                    
                      loading ...
                   """)
        time.sleep(.4)
        clear()

        print("""  
              









              
                              xx  x                               
                              xx   x                                       
                              xxxxxxxx                                    xxx 
                              xx   x                                    
                              xx  x                  
                              xx                          
                             x   x            x x x x x x              
                            x     x        x x x x x x x xx          
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                    
                      loading .
                   """)
        time.sleep(.4)
        clear()
  
        print("""    
              









              
                              xx                                  
                              xx                                 
                            xxxxx                                    
                           x  xx x                                    
                          x   xx  x                            
                              xx                          
                             x   x            x x x x x x              
                            x     x        x x x x x x x xx          
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                    
                      loading ..
                   """)
        time.sleep(.5)
        clear()

        print("""    
              



              





              
                                 xx                                  
                                 xx                                 
                               xxxxx                                    
                              x  xx x                                    
                               x xx  x                            
                                 xx                          
                                x   x         x x x x x x              
                               x    x      x x x x x x x xx          
                      ddddddddddddddddddddddddddddddddddddddddddddddddddddddd                                    
                      loading ...
                   """)
        time.sleep(.5)
      



def rip():
    clear()
    loop=0
    while loop<3:
        loop+=1
        


        print("""
              

              
              
                                                                              dddddddd              
                                                                            hh::MMMM::hh            
                                          MM                              hh::  ::::  ::hh          
                                          MM                              ::            ::          
                                          MM                                                        
                                          MM                                                        
                                          MM                                          yyyyyyyy      
                                 yyyyyyyyyMMyyyyyyyyy                                yy//MMMM//yy    
                                 +++++++++MM+++++++++                              ss++  ++++  ++ss  
                                          MM                                       ++            ++  
                                          MM                                                        
                                          MM                                                        
                                          MM                                                       
                                          MM        ////////                                        
                                          MM      //yyyyyyyy//                                      
                                          MM      MM        MM                                      
                                          MM      MM  ::::  MM                                      
                                          MM      MM  MMMM  MM                                      
                                          MM      MM  MMMM  MM                                      
                        ------------------MM------MM--MMMM--MM                                                                                                         
                   """)

        time.sleep(.5)
        clear()

        print("""
              

                                                                          dd            dd          
                                                                          --dd        dd--          
                                                                            --dddddddd--            
                                                                              ::MMMM::              
                                          MM                                    ::::                
                                          MM                                                        
                                          MM                                      yy            yy  
                                          MM                                      //yy        yy//  
                                          MM                                        //yyyyyyyy//    
                                 yyyyyyyyyMMyyyyyyyyy                                 //MMMM//      
                                 +++++++++MM+++++++++                                   ++++        
                                          MM                                                        
                                          MM                                                        
                                          MM                                                        
                                          MM
                                          MM        ////////                                        
                                          MM      //yyyyyyyy//                                      
                                          MM      MM        MM                                      
                                          MM      MM  ::::  MM                                      
                                          MM      MM  MMMM  MM                                      
                                          MM      MM  MMMM  MM                                      
                        ------------------MM------MM--MMMM--MM                                      
                                                                                                                                                            
        """)                                                                                            
                                                                                                    
        time.sleep(.5)
        clear()   