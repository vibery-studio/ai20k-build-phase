# Mẹo từ Coach: Dùng AI trợ lý viết docs cho A20

Chào các bạn! Mình chia sẻ một trick nhỏ giúp các bạn đỡ đau đầu với mấy cái JOURNAL.md, WORKLOG.md, PR format mà thầy yêu cầu.

Ý tưởng đơn giản: cho AI tool (Claude Code, Cursor, Codex...) hiểu luật chơi của khóa học → nó tự giúp bạn viết đúng format, tự đọc git log điền sẵn → bạn chỉ cần bổ sung ý kiến cá nhân.

## Cài đặt (2 phút)

**Bước 1:** Tải folder `a20` từ `resources/.claude/skills`

**Bước 2:** Bỏ vào repo project của bạn, tùy tool đang dùng:

| Tool | Bỏ vào đâu |
|---|---|
| Claude Code | `.claude/skills/a20/` |
| Cursor | `.cursor/skills/a20/` |
| Codex | `.codex/skills/a20/` |
| Gemini CLI | `.gemini/skills/a20/` |
| Copilot | `.github/skills/a20/` |

```bash
# Ví dụ cho Claude Code:
mkdir -p .claude/skills
cp -r a20 .claude/skills/
```

Xong. Không cần config gì thêm.

## Rồi dùng thế nào?

Chat bình thường với AI thôi, tiếng Việt luôn:

```
viết journal tuần này giùm mình
```

```
mình vừa quyết định dùng SQLite thay JSON, ghi ADR giùm
```

```
check mình đủ yêu cầu tạo PR chưa
```

```
tạo PR giùm
```

AI sẽ tự đọc git history điền sẵn phần nó biết, hỏi bạn mấy câu ngắn về cảm nhận cá nhân, rồi hiện draft cho bạn duyệt trước khi ghi.

## Nhắc nhỏ

- Cuối tuần nhớ viết journal (nói `viết journal` là xong)
- Quên mấy tuần cũng không sao, nói `viết journal 3 tuần gần nhất`
- Trước khi tạo PR → nói `check PR` để AI kiểm tra giùm
- AI **không tự ghi file** — luôn hỏi bạn OK chưa rồi mới ghi

Đây chỉ là tool hỗ trợ, không thay thế việc bạn suy nghĩ và viết. AI điền data, bạn điền insight. Chúc các bạn code vui!
