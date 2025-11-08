# How to Share Work with ChatGPT

This guide provides best practices and strategies for effectively collaborating with ChatGPT on your work items.

## Table of Contents
- [Getting Started](#getting-started)
- [Preparing Your Work Item](#preparing-your-work-item)
- [Effective Communication](#effective-communication)
- [Code Collaboration](#code-collaboration)
- [Review and Iteration](#review-and-iteration)
- [Common Patterns](#common-patterns)

---

## Getting Started

### 1. Define Your Work Item Clearly
Before engaging ChatGPT, clearly define:
- **What** needs to be done
- **Why** it's important
- **What** success looks like
- **When** it needs to be completed

### 2. Gather Context
Collect all relevant information:
- Code files and snippets
- Error messages or logs
- Requirements or specifications
- Previous attempts or related work

### 3. Set Expectations
Be clear about:
- Time constraints
- Technical constraints
- Quality standards
- Deliverable format

---

## Preparing Your Work Item

### Use the Work Item Template
Start with the provided template (`WORK_ITEM_TEMPLATE.md`) and fill in all sections:

```markdown
## Work Item: [Descriptive Title]

**Priority**: [High/Medium/Low]
**Status**: [Not Started]
**Created**: [Today's Date]
```

### Include Specific Details
The more specific you are, the better the assistance:

**Good Example:**
```
Task: Optimize SQL query in getUserOrders function
File: src/controllers/userController.js, line 45
Issue: Query takes 3-5 seconds for users with 1000+ orders
Database: PostgreSQL 14
Expected: Reduce to under 500ms
```

**Poor Example:**
```
Task: Make the app faster
```

---

## Effective Communication

### Ask Specific Questions
**Good:**
- "How can I optimize this SQL query to reduce execution time from 3s to under 500ms?"
- "What's the best way to implement pagination for large datasets in Express.js?"
- "Can you review this authentication middleware for security issues?"

**Less Effective:**
- "How do I make this better?"
- "Fix my code"
- "This doesn't work"

### Provide Context in Stages
1. **Start with the overview**: What you're trying to accomplish
2. **Share the details**: Code, errors, requirements
3. **Ask specific questions**: What you need help with

### Example Interaction Flow

**You:** "I'm working on optimizing database queries in a Node.js application. The getUserOrders function is slow for users with many orders."

**Then:** Share the relevant code, explain what you've tried, and ask for specific recommendations.

**Finally:** Implement suggestions, test, and report results back for further iteration.

---

## Code Collaboration

### Sharing Code Effectively

#### 1. Use Code Blocks
Always use proper formatting:

\`\`\`javascript
// Your code here
function getUserOrders(userId) {
  // implementation
}
\`\`\`

#### 2. Include Context
- File path: `src/controllers/userController.js`
- Line numbers: Lines 45-67
- Related files: Link to models, configs, etc.

#### 3. Share Error Messages
Include complete error messages and stack traces:

\`\`\`
Error: Connection timeout
  at Connection.connect (database.js:45)
  at getUserOrders (userController.js:67)
\`\`\`

### Requesting Code Reviews

Structure your review request:
```
## Code Review Request

**Purpose**: [What the code does]
**Concerns**: [What you're worried about]
**Focus Areas**: [What to review - security, performance, style]

[Code here]

**Questions**:
1. Are there any security vulnerabilities?
2. Can this be optimized?
3. Is the error handling sufficient?
```

### Getting Implementation Help

When asking for implementation:
1. Describe the requirement
2. Share relevant existing code
3. Specify constraints (libraries, patterns, etc.)
4. Ask for explanation along with code

---

## Review and Iteration

### Iterative Improvement Process

1. **Initial Request**
   - Share your work item
   - Get initial recommendations

2. **Implement and Test**
   - Try the suggestions
   - Test thoroughly
   - Document results

3. **Report Back**
   - Share what worked
   - Share what didn't
   - Ask follow-up questions

4. **Refine**
   - Iterate on the solution
   - Address edge cases
   - Optimize further

### Example Iteration

**Round 1:**
```
Me: Here's my query that's slow. How can I optimize it?
ChatGPT: Add these indexes and use pagination.
```

**Round 2:**
```
Me: I added the indexes. It's faster but still 1.5s. Here are the EXPLAIN results.
ChatGPT: The query plan shows a sequential scan. Try this JOIN optimization.
```

**Round 3:**
```
Me: Great! Down to 400ms. Now I need to handle edge cases for deleted orders.
ChatGPT: Here's how to add a soft delete filter efficiently.
```

---

## Common Patterns

### Pattern 1: Debugging
```
1. Share the error
2. Share relevant code
3. Share what you've tried
4. Ask for debugging approach
5. Implement suggestions
6. Report results
```

### Pattern 2: Design Decision
```
1. Explain the problem
2. Share constraints
3. Ask for approach recommendations
4. Discuss trade-offs
5. Choose approach
6. Get implementation help
```

### Pattern 3: Code Review
```
1. Share complete code
2. Explain purpose and context
3. Request specific feedback
4. Address findings
5. Get second review
6. Finalize
```

### Pattern 4: Learning
```
1. Ask for explanation of concept
2. Request examples
3. Try implementing
4. Share your implementation
5. Get feedback
6. Iterate until mastered
```

---

## Tips for Success

### Do's ✅
- Be specific and detailed
- Provide complete context
- Share actual code and errors
- Ask follow-up questions
- Iterate on solutions
- Document learnings
- Test suggestions thoroughly

### Don'ts ❌
- Don't be vague
- Don't skip context
- Don't expect mind-reading
- Don't ignore edge cases
- Don't accept solutions blindly
- Don't forget to test
- Don't skip documentation

---

## Advanced Techniques

### Using ChatGPT for Different Tasks

#### 1. Architecture Review
Share high-level design, ask for:
- Scalability concerns
- Security considerations
- Alternative approaches
- Best practices validation

#### 2. Performance Optimization
Provide:
- Current metrics
- Code implementation
- Profiling results
- Target metrics

#### 3. Refactoring
Share:
- Code to refactor
- Quality issues
- Desired improvements
- Constraints

#### 4. Testing Strategy
Discuss:
- What to test
- How to test
- Edge cases
- Test structure

---

## Tracking Progress

### Update Your Work Item
After each collaboration session, update the work item:

```markdown
### ChatGPT Collaboration Notes

**Session 1 (2024-11-08):**
- Discussed query optimization
- Implemented composite index
- Result: 70% performance improvement

**Session 2 (2024-11-08):**
- Addressed edge cases
- Added error handling
- Result: Production-ready code
```

### Maintain a Decision Log
Document important decisions:
- Why a particular approach was chosen
- What alternatives were considered
- Trade-offs accepted
- Performance benchmarks

---

## Example: Complete Workflow

### Starting the Work
```markdown
## Work Item: Fix Memory Leak in WebSocket Handler

**Priority**: High
**Status**: Not Started

I'm seeing memory usage increase over time in our Node.js WebSocket server.
Need to identify and fix the leak.

**Context**:
- Node.js v18
- Using 'ws' library
- Memory grows 10MB/hour
- 1000+ concurrent connections
```

### First Collaboration
"I have a memory leak in my WebSocket server. Here's the handler code: [code].
Can you help identify potential memory leaks?"

### Iteration
"I implemented your suggestion to remove listeners. Memory is still growing.
Here's the updated code and heap snapshot comparison: [data]"

### Resolution
"Fixed! The issue was event listeners not being removed on disconnect.
Added cleanup in close handler. Memory stable after 24h test."

### Documentation
Update work item with:
- Root cause
- Solution implemented
- Testing results
- Lessons learned

---

## Conclusion

Effective collaboration with ChatGPT is about clear communication, iterative improvement, and thorough testing. Use the templates and patterns in this guide to structure your work items and get the most value from AI assistance.

Remember: ChatGPT is a tool to augment your skills, not replace your judgment. Always review, test, and validate suggestions before deploying to production.
