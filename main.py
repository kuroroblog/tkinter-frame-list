import tkinter as tk

class Application(tk.Frame):
    # panedwindowを取得する関数
    def getPanedWindow(self):
        # Windowを親要素として、panedwindow Widget(Frame)を作成する。
        # <用語の説明>
        # panedwindow Widget(Frame)の中に配置される、Widgetのことを「ペイン」という。
        # ペインとペインの間の空間を「さっし」という。さっしを選択した状態で、さっしを左右(上下)へ動かすとWidget(ペイン)の大きさを自由に変更できる。
        # また、さっしの中に表示される、四角いものを「handle」という。handleはさっしと同じ動作を行う。
        # showhandle : さっしの中へhandleを表示するかどうかの設定。True : 表示する, False : 表示しない。
        # sashwidth : さっしの幅を設定。
        # PanedWindowについて : https://kuroro.blog/python/0KVm0XNc0gvKrbM4O9bD/
        panedWindow = tk.PanedWindow(self.master, showhandle=True, sashwidth=20)
        # Windowを親要素として、panedwindow Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        panedWindow.pack()

        # panedwindow Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label1 = tk.Label(panedWindow, text="test", width=10, bg="#008000")
        # panedwindow Widget(Frame)を親要素として、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label1.pack()

        # panedwindow Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label2 = tk.Label(panedWindow, text="test", width=10, bg="red")
        # panedwindow Widget(Frame)を親要素として、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label2.pack()

        # label Widget要素をpanedwindow Widget(Frame)へ格納。ペインとする。
        # add(Widget) : Widgetをpanedwindow Widget(Frame)へ格納する。
        panedWindow.add(label1)
        # label Widget要素をpanedwindow Widget(Frame)へ格納。ペインとする。
        # add(Widget) : Widgetをpanedwindow Widget(Frame)へ格納する。
        panedWindow.add(label2)

    # labelframeを取得する関数
    def getLabelFrame(self):
        # Windowを親要素として、labelframe Widget(Frame)を作成する。
        # text : ラベルの設定。labelframeとする。
        # LabelFrameについて : https://kuroro.blog/python/ggEa100zNeLfl5nJg1iK/
        labelframe = tk.LabelFrame(self.master, text='labelframe')
        # Windowを親要素として、labelframe Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        labelframe.pack()

        # labelframe Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label1 = tk.Label(labelframe, text="test", width=10, bg="#008000")
        # labelframe Widget(Frame)を親要素として、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label1.pack()

        # labelframe Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label2 = tk.Label(labelframe, text="test", width=10, bg="red")
        # labelframe Widget(Frame)を親要素として、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label2.pack()

    # frameを取得する関数
    def getFrame(self):
        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label1 = tk.Label(frame, text="test", width=10, bg="#008000")
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label1.pack()

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # bg : 背景色の設定
        # 色について : https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label2 = tk.Label(frame, text="test", width=10, bg="red")
        # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label2.pack()

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")
        # self.getFrame()
        # self.getLabelFrame()
        # self.getPanedWindow()

# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを作成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()
    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
