import fresh_tomatoes
import media


titanic = media.Movie("Titanic", "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic. ",
                          "https://goo.gl/1VFvnz",
                          "https://www.youtube.com/watch?v=zCy5WQ9S4c0")


lord_of_the_rings = media.Movie("Lord of The Rings",
                                 "A meek Hobbit from the Shire and eight companions setout on a journey to destroy the powerful One Ring and save Middle-earth from the Dark Lord Sauron",
                                  "https://imgc.allpostersimages.com/img/print/posters/lord-of-the-rings-fellowship-of-the-ring_a-L-8678123-0.jpg",
                                  "https://www.youtube.com/watch?v=V75dMMIW2B4")

Sweeney_Todd = media.Movie("Sweeney Todd: The Demon Barber of Fleet Street",
                            "The infamous story of Benjamin Barker, aka Sweeney Todd, who sets up a barber shop in London which is the basis for a sinister partnership with his fellow tenant, Mrs. Lovett.",
                            "https://goo.gl/mQAk99",
                            "https://www.youtube.com/watch?v=AP_nk--zCZY")
saw = media.Movie("Saw", "Two strangers, who awaken in a room with no recollection of how they got there, soon discover they're pawns in a deadly game perpetrated by a notorious serial killer. ",
                   "https://goo.gl/roixHW",
                   "https://www.youtube.com/watch?v=S-1QgOMQ-ls")
bad_words = media.Movie("Bad Words","A spelling bee loser sets out to exact revenge by finding a loophole and attempting to win as an adult.",
                         "https://goo.gl/xkhEJh", "https://www.youtube.com/watch?v=erM_EksoVPc")
thirty_days = media.Movie("30 Days of Night", "After an Alaskan town is plunged into darkness for a month, it is attacked by a bloodthirsty gang of vampires. ",
                           "https://goo.gl/RuPnw8","https://www.youtube.com/watch?v=zXYO19Ig5hc")


#lord_of_the_rings.show_trailer()
movies = [titanic,lord_of_the_rings,Sweeney_Todd,saw,bad_words,thirty_days]
#fresh_tomatoes.open_movies_page(movies)
print (media.Movie.__module__)
