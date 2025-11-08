# Quick Start Guide - SHAREWORK

Get started with sharing work with ChatGPT in 5 minutes!

## Step 1: Choose Your Work Item

Identify what you need help with:
- 🐛 Bug fix
- 🚀 New feature
- 📊 Code optimization
- 📝 Documentation
- 🎨 Refactoring
- 🔒 Security review
- 🧪 Testing

## Step 2: Create Your Work Item

Copy the template:
```bash
cp WORK_ITEM_TEMPLATE.md my_work_item.md
```

Fill in the details:
```markdown
## Work Item: Fix Login Bug

**Priority**: High
**Status**: Not Started
**Created**: 2024-11-08

### Description
Users cannot login with email addresses containing + symbols

### Context
- Using Node.js with Passport.js
- Email validation regex appears to be rejecting valid emails
- Reported by 15 users

### Tasks
- [ ] Identify validation logic
- [ ] Fix regex pattern
- [ ] Add tests for edge cases
- [ ] Deploy fix

### Expected Outcome
All valid email addresses can be used for login
```

## Step 3: Start Collaborating with ChatGPT

### Share Your Work Item
1. Open your conversation with ChatGPT
2. Say: "I'm using SHAREWORK to track my tasks. Here's my work item:"
3. Paste your work item content
4. Ask specific questions

### Example Opening
```
Hi! I'm working on fixing a login bug. Here's my work item:

[Paste work item]

Can you help me identify why the email validation might be 
rejecting emails with + symbols?
```

## Step 4: Iterate and Track Progress

### Update Status
As you make progress, update your work item:
```markdown
**Status**: In Progress → Review → Completed
```

### Check Off Tasks
```markdown
- [x] Identify validation logic ✅
- [x] Fix regex pattern ✅
- [ ] Add tests for edge cases (working on this)
- [ ] Deploy fix
```

### Document Collaboration
```markdown
### ChatGPT Collaboration Notes

**Session 1:**
- ChatGPT identified regex pattern: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/
- Issue: + symbol in character class needs escaping
- Fixed regex: /^[A-Z0-9._%+\-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i
```

## Step 5: Complete and Review

### Before Closing
- [ ] All tasks completed
- [ ] Code tested
- [ ] Documentation updated
- [ ] Changes deployed
- [ ] Work item marked as completed

### Learn from the Process
Document what you learned for future reference:
```markdown
### Lessons Learned
- Email regex should follow RFC 5322 standard
- Always test with edge cases (special characters)
- ChatGPT helped identify the regex issue in 2 minutes!
```

---

## Real-World Example

### The Problem
```
"My API is slow when fetching user data"
```

### The Work Item
```markdown
## Work Item: Optimize User Data API

**Priority**: High
**Status**: In Progress

### Description
GET /api/users/:id endpoint takes 2-3 seconds to respond

### Context
- 50,000 users in database
- Response includes user profile, orders, and preferences
- Using MongoDB
- No caching implemented

### Tasks
- [x] Profile the query
- [x] Identify N+1 query problem
- [ ] Implement aggregation pipeline
- [ ] Add Redis caching
- [ ] Test performance

### Expected Outcome
Response time under 200ms for 95% of requests
```

### The Collaboration
```
Me: I have a slow API endpoint. Here's my current implementation: [code]

ChatGPT: I see you're making multiple database calls. Use MongoDB 
aggregation to fetch related data in one query: [solution]

Me: Implemented aggregation. Now at 800ms. Still need faster.

ChatGPT: Add Redis caching for user data with 5-minute TTL: [code]

Me: Perfect! Now at 150ms average. Thanks!
```

---

## Tips for First-Time Users

### Start Small
- Pick a simple task for your first work item
- Get comfortable with the process
- Build confidence before tackling complex issues

### Be Specific
Instead of: "Fix my code"
Try: "Fix the email validation regex in auth.js to accept + symbols"

### Provide Context
Share:
- What you're trying to do
- What's not working
- What you've tried
- Error messages or logs

### Ask Follow-Up Questions
Don't stop at the first answer:
- "Why does this approach work better?"
- "What are the trade-offs?"
- "Are there edge cases I should consider?"

---

## Common Use Cases

### 1. Code Review
```
"Please review this function for security issues and performance:
[code]"
```

### 2. Debugging
```
"I'm getting this error: [error]
Here's my code: [code]
What could be causing this?"
```

### 3. Implementation
```
"I need to implement JWT authentication in Express.js.
Requirements: [list]
Can you provide an example?"
```

### 4. Optimization
```
"This query is slow: [code]
Database: PostgreSQL
Table size: 1M rows
How can I optimize it?"
```

### 5. Learning
```
"Can you explain how async/await works in JavaScript?
Then show me an example of converting this callback code: [code]"
```

---

## Next Steps

1. **Read the Full Guide**: Check out `COLLABORATION_GUIDE.md` for advanced techniques
2. **Explore Examples**: Review the examples in the `examples/` directory
3. **Start Your First Work Item**: Create your work item and start collaborating!
4. **Share Your Experience**: Update this repo with your learnings

---

## Need Help?

- 📖 Read: `COLLABORATION_GUIDE.md` for detailed strategies
- 👀 See: `examples/` directory for real work item examples
- 📋 Use: `WORK_ITEM_TEMPLATE.md` to structure your work
- 💡 Tip: The more context you provide, the better the help you'll receive

---

## Success Metrics

You're doing it right when:
- ✅ Your work items are well-structured
- ✅ You're getting actionable help from ChatGPT
- ✅ You're iterating and improving solutions
- ✅ You're documenting learnings
- ✅ You're completing tasks faster than before

Happy collaborating! 🚀
