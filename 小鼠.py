import customtkinter as ctk
import math
import tkinter as tk

# 界面基础设置
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
app = ctk.CTk()
app.title("老鼠测毒计算器")
app.geometry("400x550")

# 界面控件搭建
input_frame = ctk.CTkFrame(app, fg_color="transparent")
input_frame.pack(pady=15)

label_sl = ctk.CTkLabel(input_frame, text="水的总数量：", font=("", 16))
label_sl.pack(side="left", padx=5)

entry_sl = ctk.CTkEntry(input_frame, width=120, font=("", 16))
entry_sl.pack(side="left")

btn_start = ctk.CTkButton(app, text="开始", width=200, height=35, font=("", 16, "bold"))
btn_start.pack(pady=5)

# 用文本框代替原本的黑框 print 输出
output_box = ctk.CTkTextbox(app, width=350, height=400, font=("Consolas", 14))
output_box.pack(pady=10)


def run():
    output_box.delete("1.0", tk.END)  # 清空上次结果
    try:
        sl = entry_sl.get()       # 获取输入
        sl = int(sl)              # 转成整数
    except ValueError:
        output_box.insert("end", "请输入纯数字！\n")
        return

    # ==========================================
    # 以下是你原汁原味的代码风味，完全没动：
    # ==========================================
    def er(sl):
        if sl == 0:
            return "0"
        se = ""
        while sl > 0:
            se = str(sl % 2) + se
            sl = sl // 2
        return se

    if sl > 0:
        k = math.log2(sl)
    else:
        k = 0
    k = math.ceil(k)

    for bottle in range(sl):
        b = er(bottle).zfill(k)
        # 把 print(bottle,b) 换成写入文本框
        output_box.insert("end", f"{bottle} {b}\n")
    
    # 把 time.sleep(1) 换成 GUI 延迟，不卡死窗口
    def show_result():
        output_box.insert("end", f"需要{k}只老鼠\n")
        output_box.see("end")  # 自动滚动到底部
    
    app.after(1000, show_result)  # 延迟 1000 毫秒（即1秒）执行
    # ==========================================

# 绑定按钮事件
btn_start.configure(command=run)

# 运行
app.mainloop()