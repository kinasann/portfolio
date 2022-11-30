import streamlit as st
from PIL import Image

st.write('<h6 style="color:white">Top</h6>', unsafe_allow_html=True)
st.title("ポートフォリオ")


st.write('<font size="8"><b>tkinter Tool</font></b> <nobr>&emsp;&emsp;&emsp;\
        <a href="https://github.com/kinasann/portfolio/blob/main/tkinter_Tool.zip?raw=true">\
        ダウンロード</a>', unsafe_allow_html=True)



with st.sidebar:
        st.write('<a href="#python-50">■ 使用言語、制作時間、使用モジュール</a>', unsafe_allow_html=True)
        st.write('<a href="#content">■ 内容</a>', unsafe_allow_html=True)
        st.write('<a href="#trigger">■ 作成に至ったきっかけ</a>', unsafe_allow_html=True)
        st.write('<a href="#purpose">■ 目的、趣旨</a>', unsafe_allow_html=True)
        st.write('<a href="#devised">■ 特に工夫したところ</a>', unsafe_allow_html=True)
        with st.expander("各項目事の内容、工夫した点"):
                st.write('<a href="#left-window">★左ウインドウを</a>', unsafe_allow_html=True)
                st.write('<a href="#geomentry">★geometry</a>', unsafe_allow_html=True)
                st.write('<a href="#place">★place配置</a>', unsafe_allow_html=True)
                st.write('<a href="#color">★color</a>', unsafe_allow_html=True)
        st.write('<div style="text-align: right"><a href="#top">一番上へ</a></div>',
                unsafe_allow_html=True)
        st.write('<div style="text-align: right">\
                <a href="https://github.com/kinasann/portfolio/blob/main/tkinter_Tool.zip?raw=true">\
                tkinter Tool ダウンロード</a></div>', unsafe_allow_html=True)

img_top = Image.open('tkinter_tool top.png')
st.image(img_top, caption="tkinter Tool起動時", use_column_width=True)


st.write('<h4 id=python>■ 使用言語 &emsp; Python &emsp;&emsp; &emsp;&emsp; ■ 制作時間 &emsp; 約50時間</h4>', unsafe_allow_html=True)
st.write('<h4>■ 使用モジュール</h4>', unsafe_allow_html=True)
st.write("&nbsp;tkinter ,&nbsp; pyperclip (コピー用) &nbsp;, OS (画像読み込み用)", unsafe_allow_html=True)
st.write("")

st.write('<h6 style="color:white">content</h6>', unsafe_allow_html=True)
st.write('<h4>■ 内容</h4>', unsafe_allow_html=True)
"""
tkinterでデスクトップアプリを作る際に活用できるツールアプリ
画面の右端にメニュー画面を固定し、対象のボタンを押すことで調べることが出来る。
アプリを立ち上げると、左画面にヘルプが表示。右側にメニューが表示される。
"""

st.write('<h6 style="color:white">Trigger</h6>', unsafe_allow_html=True)
st.write('<h4>■ 作成に至ったきっかけ</h4>', unsafe_allow_html=True)
st.write("・tkinterでデスクトップアプリを作る際に、geometryやplaceの引数を目安で記入し、実行して確かめる → \
        思うサイズや位置ではなく、再度記入と実行…  等、微調整を繰り返すことが多かった。")
st.write("・色を設定する場合、redなどの単語指定ではなく、好みの色を設定する場合、毎回インターネットで検索する必要があった。")
st.write("上記のような微調整に時間が掛かり、制作がなかなか進まず、一目でわかるようなツールがあれば作りやすいのではないかと思い、\
        今回の作成に至った。")

st.write('<h6 style="color:white">Purpose</h6>', unsafe_allow_html=True)
st.write('<h4>■ 目的、趣旨</h4>', unsafe_allow_html=True)
st.write("・geometry引数 → ウインドウを好きなサイズや位置に動かすことで、引数の入手")
st.write("・place引数 → ルーラーを作成し、照らし合わせることで座標がわかる")
st.write("・color →色選択ダイアログで好きな色を選択し、カラーコードを入手")

st.write('<h6 style="color:white">devised</h6>', unsafe_allow_html=True)
st.write('<h4 id="a">■ 特に工夫したところ</h4>', unsafe_allow_html=True)
st.write("・シンプルで使いやすいアプリになるよう心掛けた。")
st.write("・右端のメニューウインドウがメインウインドウ。左側に出る各ウインドウがサブウインドウに設定。\
        左側にウインドウが展開したままであっても、メニューウインドウを閉じると全てのウインドウが閉じてアプリが終了する")
st.write("・コピーボタンの作成")
st.write("・placeルーラー(透過処理、背景変更、テキストボックスを使用したウインドウ展開等)")
st.write("・ヘルプウインドウの作成")
st.write("")
st.write("")
st.write("")
st.write("各項目事の内容、工夫した点の詳細は下記にて説明")
st.write("")

st.write('<h6 style="color:white">left window</h6>', unsafe_allow_html=True)
st.write('<h5>★左ウインドウを</h5>', unsafe_allow_html=True)
st.write("<b>閉じるボタン：</b> 文字通りメニューウインドウ左に展開されるウインドウを閉じることが出来る。<br>\
        左側にウインドウが展開されていない場合は、押すことはできるが何も反応はない。",unsafe_allow_html=True)
st.write("")
st.write('<h6 style="color:white">geometry</h6>', unsafe_allow_html=True)
st.write('<h5>★geometry</h5>', unsafe_allow_html=True)
img_geo =Image.open("geo_pic.png")
st.image(img_geo, caption="geometry", use_column_width=True)

st.write("<b>ウインドウ作成：</b> 左側にウインドウを展開 <br> 通常のウインドウ操作と同様、\
        ドラッグすることで大きさ変更、ウインドウ位置の移動をすることができる。",unsafe_allow_html=True)

st.write('<b>確認ボタン：</b> 色選択ダイアログ以外の左側に展開しているウインドウの現在のサイズ、\
        位置をテキストボックスに代入<br><span style="border-bottom:solid 3px #ff8040;">ウインドウ横幅\
        </span> x<span style="border-bottom:solid 3px #0000ff;">ウインドウ縦幅</span> x \
        <span style="border-bottom:solid 3px #ff80c0;">PC画面左端からウインドウまでの幅</span> x \
        <span style="border-bottom:solid 3px #00b050;">PC画面上端からウインドウまでの幅</span><br>\
        geometryの引数に設定することで、同じサイズと位置でウインドウを作ることが出来る。', unsafe_allow_html=True)

st.write("<b>コピーボタン：</b>文字通りコピーすることができるボタン<br>\
        コピー対象はgeometryラベルフレーム内のテキストボックス全範囲になっているため、\
        一部分のみやplace位置ラベルフレーム内のテキストボックスをコピーすることは不可能<br>\
        もし一部分のみコピーしたい場合は、コピーボタンは使用せず、通常通りテキストボックス内のコピーしたい範囲をドラックして\
        「ctrl + c」することでコピーすることは可能",unsafe_allow_html=True)
st.write("")

st.write('<h6 style="color:white">place</h6>', unsafe_allow_html=True)
st.write('<h5>★place配置</h5>', unsafe_allow_html=True)
st.write("ウィジットを配置するときに使用するメソッドの一つであるplaceの座標をわかりやすく表示する物差し(ルーラー)のようなもの。")

img_place =Image.open("place.png")
st.image(img_place, use_column_width=True)
st.write('<span style="color:#808080;">&emsp;&emsp;&emsp;&emsp; 縦軸(x=) \
        &emsp;&emsp;&emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; \
        横軸(y=)&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; \
        方眼(x= ,y=)</span>', unsafe_allow_html=True)

st.write("placeは1ピクセルごとに設定されているため、10ピクセルごとにラインを設定。<br>\
        基本の線(10ピクセル単位)は青線、50ピクセル単位を緑線、100ピクセル単位を赤線に設定し、1000ピクセルの値には太線を引いている。<br>\
        ウインドウを好きなサイズに変更できるようパソコン画面のサイズをプログラムが取得し、最大化してもルーラーの線が途切れないように設定している。",
        use_column_width=True)
st.write("作成中のウインドウを照らし\
        合わせやすいように、ルーラー部分は透過処理を行っている。<br>\
        そのためルーラー部分がすり抜けてしまい、サイズ調整がしづらい課題があった。<br>\
        透過処理をしていないタイトルバーと目盛部分にカーソルを合わせて調整することで通常通り出来るが、\
        どの部分でも調整ができる方がいいだろうと考え、スペースキーを押している間は背景色が変わるように設定。",
        unsafe_allow_html=True)

img_touka = Image.open("place_s.png")
st.image(img_touka, use_column_width=True)


st.write("また、作成しているウインドウサイズや位置が決まっている場合はテキストボックスに記入して\
        調べたい軸のボタンを押すと、そのウインドウの左上に合わせた位置でルーラーが展開される")

img_touka_geo = Image.open("place_geo.png")
st.image(img_touka_geo, use_column_width=True)

st.write("このプログラムを組むにあたり、テキストボックスに代入された文字を各要素に分解、計算、結合を行っている。")
st.write("100x500などウインドウサイズのみの入力だった場合、ウインドウサイズは反映するがウインドウ位置は初期値に表示される。<br>\
        このplaceルーラーウインドウのサイズや位置もgeometryラベルフレームの確認ボタンで取得できるため、\
        調べたいウインドウと重ねて確認ボタンを押すことで、位置の確認ができる。<br>\
        その後、再度placeラベルフレームのテキスト欄に記入して対象の軸ボタンを押すと、\
        ウインドウの左上に合わせた位置でルーラーが展開される", unsafe_allow_html=True)

img_place_geo = Image.open("place_plus_geo.png")
st.image(img_place_geo, use_column_width=True)
st.write("")

st.write('<h6 style="color:white">color</h6>', unsafe_allow_html=True)
st.write('<h5>★color</h5>', unsafe_allow_html=True)
st.write("<b>色ボタン：</b>ボタンを押すと、色選択ダイアログが表示 <br>\
        本アプリ以外時の色選択ダイアログと同様、基本色にない色も設定することが出来る。<br>\
        「OK」を押すとカラーコードと書かれた下のテキストボックスにコードが代入。<br>\
        また、色ボタン右に選択した色を表示するように設定している。<br>", unsafe_allow_html=True)
st.write("<b>コピーボタン：</b>geometryと同様、カラーコードと書かれた下のテキストボックス内全てがコピー対象になる     ",unsafe_allow_html=True)


img_color = Image.open("color2.png")
st.image(img_color, use_column_width=True)
