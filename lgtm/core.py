import click

# コマンドとして実行したい関数に@click.command
# 名前を付けたオプションで渡すものは@click.option
# 位置引数として渡すものは@click.argument
@click.command()
@click.option("--message", "-m", default="LGTM", show_default=True, help="画像に乗せる文字列")
@click.argument("keyword")
def cli(keyword, message):
    # LGMT画像生成ツール
    lgtm(keyword, message)
    click.echo("lgtm")


def lgtm(keyword, message):
    pass
