# Reversi-AlphaZero
AlphaZeroの機械学習アルゴリズムを参考に作成したオセロゲーム
  
```python
from google.colab import files
uploaded = files.upload()

!python TrainCycle.py

from google.colab import files
files.download('./model/best.h5')
```



## Game.py
オセロの基本ルール設定
## ResidualNetwork.py
Residual Network(ResNet)の構築
## MonteCarloTreeSearch.py
モンテカルロ木探索プログラム
## SelfPlay.py
過去最強のプレイヤー同士で対戦させ学習データを作成する
## TrainNetwork.py
`SelfPlay.py`で作成された学習データを使ったResidual Network(ResNet)での学習
## EvaluateNetwork.py
最新プレイヤーと過去最強のプレイヤーを対戦させ強い方を残すプログラム
## TrainCycle.py
全てのスクリプトを合わせた学習サイクルの構築
## HumanPlay.py
プログラムで作成されたAIとの対戦
