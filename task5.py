good = r"""
      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|


"""
bad = r"""

         *                       *
            *                 *
           )       (\___/)     (
        * /(       \ (. .)     )\ *
          # )      c\   >'    ( #
           '         )-_/      '
         \\|,    ____| |__    ,|//
           \ )  (  `  ~   )  ( /
            #\ / /| . ' .) \ /#
            | \ / )   , / \ / |
             \,/ ;;,,;,;   \,/
              _,#;,;;,;,
             /,i;;;,,;#,;
            ((  %;;,;,;;,;
             ))  ;#;,;%;;,,
           _//    ;,;; ,#;,
          /_)     #,;  //
                 //    \|_
                 \|_    |#\
                  |#\    -"  
                   -"

"""
escaped = False
if escaped:
    outcome = "Legend: You have made it to the other side! "
    print({good})
else:
    outcome = "Doom: You've crossed the bridge just to snap your ankle on the last step and fall to your death... Really?"
    print({bad})
print(f"{outcome}")