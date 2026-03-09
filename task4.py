good = r"""

               .-""-..   __       .--.
             .-.`( >  ""- ,)_    (   (
              `_( >    ~<| 0)-')')---')
            -."_( >     ~<`-"  " "  vV
            -._( >    -._ <  .___.Y'
             `._( >    `._(  ((        .
              '-._( >  '-._(  \\__^_^,';
                .-( >      ~<  .-.-.-./
               '--._( >       { v V Y
                   .-< >       \
                    "-< >       \   (PS)

"""
bad = r'''

                          __..__             
                      _.sMSMMMMMMb.          
                   .-"TMMMMSMMMMMMMb.    
                 .'    TMMMMSMMMMMMMMb       
                /       TMMMSMMMMMMSSS;      
               :        :MMMMSMMMSSMMMM;     
               ;       @ MMMMSMMSMMMMMMS     
              :    _,   ,P"TMSMSMMMMMMSM     
              : .+""`,  :    `TMMMMMSSMM     
               ) c),     `-,-=,TSSSSMMMM     
              /  `         ,-;|MMMMMMMM;     
             /     _.'(o)  '-';SMSSSSSS      
            (  ,   o       ,-"'`^MMMM'       
             )`            :`.    .'         
             )-.           ;  `- /           
             \         _.-'     :            
             (     _.-"   `.     \           
              "---"--.      \     \          
                      `.     \     \         
                   bug  \       _.sSb        
                         \ _.sSSSSSSSb       
                         dSSSSSSSSP^" \      
                         SSSP^" ___    \     
                        /    .gP""""Tp. \
                       :    d'     .  `b \
                       ;   d'       o  `b ;
                      /   d;            `b|
                     /,   $;          @  `:
                    /'    $$               ;
                  .'      $$b         (o)  |
                .'       d$$$;             :
               /       .d$$$$;          ,   ;
              d      .d$$$$$$$          $   |
             :bp.__.g$$$$$$$$$         :$   ;
             $$$$$$$$$$$$$$$$$         $$b :

'''
drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: The bridge is down and ready to cross. Tread lightly..."
else:
    outcome = "Doom: The bridge remains raised and the chasm below takes you..."
print(f"{outcome}")