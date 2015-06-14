# chess-greymeter-hackathon
Chess logic made at Greymeter Hackathon 13-14th June 2015

##Problem Statement

###The Battle of the Kings

####The Game
1. There is a board game played between two players. The board has nXn equal squares, where 8 <= n <= 15  (similar to a chess board). 
2. Only two kings will be placed on the board at the starting of the game (one at 1,1 and second at n,n position). 
3. The kings can move one square in any direction - up, down, to the sides, and diagonally, just like chess. 
4. Each square can be visited at-most once by either of the kings.
5. The king who gets killed, or is out of moves loses the game.

####What you need to do?
1. You need to write a bot, which can play the game on your behalf. And expose this bot as a webservice.
2. Your webservice should run on port 8080 and expose three APIs:

| URL        | Type           | Parameter  |  Sample Response | Purpose |
| ------------- |:-------------:| -----:| ------------- |:-------------:|
| /ping      | GET | -- | {ok: true}  | To let us know that your bot server is alive  |
| /start      | GET      |   y,o,g |  {ok: true}  | For you to initialize the round. Here y would indicate position of your king (eg: 1&#1241), o indicates position of opponent’s king (eg: n&#124n), and g indicates size of the grid.  |
| /play | GET      |    m | {m:”1&#1242”} | m : Move made by your opponent. Your response would convey your next move.  |

Note: By convention all positions are represented as x|y where x and y are respective coordinates on the board. Bottom left board is 1|1.

####The Rules
1. At the beginning, all players would be given a rating of 8.
2. After a game, half of the rating points of losing player would be transferred to the winning player.
3. For first game between any two players, each of the player will be awarded one additional rating point.
4. A game will consist of two rounds with each player getting the first move in one round. To win a game, you need to win both the rounds. 
5. You will see the leaderboard on http://hackathon.unicommerce.com. Here you’ll be able to challenge any of the available players. A player is available for challenge if his bot server is alive and he has marked himself as “Available for Challenge”. You can mark yourself as “Available for Challenge” using the button provided on the panel.
6. At the end of each game, you will be marked as “Not Available For Challenge”. You’ll need to make yourself available for challenge to play next game. 
7. There can be at most 5 games between any two players.
8. You can see the reply of any of the games in the “Games Arena” tab.
9. As soon as one makes a move to an already visited square (by any of the king), they are declared a loser for the game.
10. If your API takes more than 3 secs to respond, or gives an invalid response, you’ll lose the game.
11. You will be disqualified if your rating points go down to 0 (after rounding off to 2 decimal places).
12. Top few players after above rounds will then fight against each other in knock-out tournament.
13. You are allowed to modify/improvise your algorithm at any time during the course of the event.
