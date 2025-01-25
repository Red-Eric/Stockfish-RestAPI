from stockfish import Stockfish

class Engine:
    def __init__(self):
        self.engine = Stockfish(path="D://Stockfish//17.exe", depth = 12)
        self.engine.set_skill_level(20)

    def get_Data(self, fen):
        if(self.engine.is_fen_valid(fen=fen)):
            #[{'Move': 'e2e4', 'Centipawn': 32, 'Mate': None}, 
            # {'Move': 'd2d4', 'Centipawn': 28, 'Mate': None}, 
            # {'Move': 'g1f3', 'Centipawn': 24, 'Mate': None}, 
            # {'Move': 'c2c4', 'Centipawn': 15, 'Mate': None}, 
            # {'Move': 'e2e3', 'Centipawn': 15, 'Mate': None}]
            self.engine.set_fen_position(fen)
            movesList = []
            evalList = []
            for move in self.engine.get_top_moves(5):
                movesList.append(move['Move'])
                if move['Mate']:
                    evalList.append(f"Mate : {move["Mate"]}")
                else:
                    evalList.append(f"Eval : {move["Centipawn"] / 100}")


            if(self.engine.get_evaluation()['type'] == "mate"):
                score = f"Mate : {self.engine.get_evaluation()['value']}"
            else:
                score = f"Eval : {self.engine.get_evaluation()['value'] / 100}"

            return {
            "score" : score,
            "bestmoves" : movesList,
            "evals" : evalList
            
            }
        else:
            return {
            "bestmoves" : ["e2e4"],
            "evals" : [0]
            }
        