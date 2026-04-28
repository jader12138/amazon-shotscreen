import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# ========== 只改这里 ==========
URL = "https://"
TOTAL_PAGE = 000
# ==============================

SAVE_DIR = "写真"
WAIT_AFTER_PAGE = 10   # 翻页后等10秒
WAIT_BEFORE_NEXT = 1   # 截图后等1秒

os.makedirs(SAVE_DIR, exist_ok=True)

# 浏览器配置
opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=opt)
driver.get(URL)

# 等待登录
input("✅ 浏览器已打开，请登录亚马逊，登录完按回车继续：")
time.sleep(3)

success = 0

# ==================== 核心程序 ====================
for page in range(1, TOTAL_PAGE + 1):
    print(f"\n📄 正在处理第 {page} 页")

    # 1. 等待12秒（菜单自动消失）
    print(f"⌛ 等待 {WAIT_AFTER_PAGE} 秒...")
    time.sleep(WAIT_AFTER_PAGE)

    # 2. 全屏截图
    save_path = os.path.join(SAVE_DIR, f"{page:03d}.png")
    driver.save_screenshot(save_path)
    print(f"✅ 第{page}页截图完成")
    success += 1

    # 3. 等待2秒
    time.sleep(WAIT_BEFORE_NEXT)

    # 4. 【终极翻页：按键盘 ← 左箭头】
    if page < TOTAL_PAGE:
        print("🔄 翻页（按左箭头）...")
        driver.find_element(by="tag name", value="body").send_keys(Keys.ARROW_LEFT)
        time.sleep(1)

# 结束
driver.quit()
print(f"\n🎉 全部完成！成功截图：{success} 张")
