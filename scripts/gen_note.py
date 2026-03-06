import os
import sys

TEMPLATE = """# {id}. {name}

## 🔗 题目链接
[LeetCode {id}. {Name}](https://leetcode.com/problems/{name}/)

## 🧠 题目描述


---

## 💡 解题思路

核心思路：

- 
- 
- 

步骤：

1. 
2. 
3. 

---

## 🧩 代码

[code](../solutions/{id}.{name}.py)


"""


def generate_note(problem_id: str):
    problems_dir = "solutions"
    notes_dir = "notes"
    os.makedirs(notes_dir, exist_ok=True)

    # 找到对应的文件
    target_file = None
    for file in os.listdir(problems_dir):
        if file.startswith(f"{problem_id}.") and file.endswith(".py"):
            target_file = file
            break

    # 提取 id 和 name
    base_name = os.path.splitext(target_file)[0]  # 去掉 .py
    parts = base_name.split(".", 1)
    id_, name = parts
    Name = name.replace("-", " ").title()  # 格式化名称

    # 生成笔记内容
    content = TEMPLATE.format(id=id_, name=name, Name=Name)

    # 输出到 notes 文件夹
    note_file = os.path.join(notes_dir, f"{id_}.{name}.md")

    # 如果笔记已存在，则取消生成
    if os.path.exists(note_file):
        print(f"⚠️ 笔记已存在，取消生成: {note_file}")
        return
    with open(note_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ 笔记已生成: {note_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python generate_note.py <题号>")
    else:
        generate_note(sys.argv[1])
