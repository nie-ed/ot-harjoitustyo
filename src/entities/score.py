import uuid


class Score:

    def __init__(self, score, score_id=None):
        """Luokan konstruktori, joka luo uuden tehtävän.
        Args:
            content: Merkkijonoarvo, joka kuvaa tehtävän sisältöä.
            done:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvastaa, onko tehtävä jo tehty.
            user:
                Vapaaehtoinen, oletusarvoltaan None.
                User-olio, joka kuvaa tehtävän omistajaa.
            todo_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa tehtävän id:tä.
        """

        self.score = score
        self.id = score_id or str(uuid.uuid4())
