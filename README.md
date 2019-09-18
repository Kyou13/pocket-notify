# pocket-notify

## Description
Pocketでその日に登録した記事をSlackに通知

## Demo
![image](https://user-images.githubusercontent.com/13377817/65143733-aa3eec00-da50-11e9-9a16-2d34d7bcfcb6.png)

## Requirement
- pipenv
- direnv
- AWS lambda
- Incoming Webhook(Slack App)

## Usage
```local
$ pipenv install
$ pipenv run python main.py
```

## Install
1. [Pocket API Documents](https://getpocket.com/developer/)に従い，`CONSUMER_KEY`, `ACCESS_TOKEN`を取得．Incoming Webhooksを有効化し，`Webhook URL`を取得.
2. [【AWS】Lambdaでpipしたいと思ったときにすべきこと](https://qiita.com/Hironsan/items/0eb5578f3321c72637b5)を参考に，Lambdaでpython外部モジュールが使えるようにする．
3. `lambda_handler`から`main`を呼び出すようにコピペする．

