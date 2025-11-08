# Work Item Example: Bug Fix

## Work Item: Fix User Session Timeout Issue

**Priority**: High  
**Status**: Review  
**Created**: 2024-11-07  
**Assigned to**: ChatGPT

---

### Description
Users are being logged out unexpectedly after 5 minutes of activity, even though the session timeout is configured for 30 minutes. This is causing frustration and lost work, especially for users filling out long forms.

---

### Context
- Issue reported by 50+ users in the past week
- Occurs across all browsers
- Session management using Express-session with Redis store
- JWT tokens used for API authentication
- Token refresh mechanism implemented
- Issue started after deployment v2.3.0 on Nov 1st

---

### Tasks
- [x] Reproduce the issue locally
- [x] Review session configuration changes in v2.3.0
- [x] Check Redis connection and session storage
- [x] Analyze JWT token expiration logic
- [x] Identify root cause (token refresh not updating Redis)
- [ ] Implement fix
- [ ] Write unit tests
- [ ] Test on staging environment
- [ ] Deploy to production

---

### Expected Outcome
- Users can maintain sessions for the full 30-minute timeout period
- Active users have their sessions automatically extended
- No data loss during normal usage
- Fix deployed without requiring user re-login
- Monitoring confirms session behavior is correct

---

### Resources
- **Files**: 
  - `server/middleware/auth.js`
  - `server/config/session.js`
  - `server/routes/auth.js`
- **Documentation**: 
  - Express-session documentation
  - Redis session store docs
  - JWT best practices guide
- **References**: 
  - Issue tracker: BUG-445
  - Deployment logs from Nov 1st
  - User reports and screenshots

---

### Notes
- Critical issue - blocking users from completing work
- Rollback not an option due to other important fixes in v2.3.0
- Need hotfix deployment window this weekend
- Monitoring shows Redis connection is stable
- Root cause: token refresh updates JWT but doesn't update Redis TTL

---

### ChatGPT Collaboration Notes

**Session 1 (2024-11-07):**
- Reviewed session configuration code
- ChatGPT identified issue: `touch` option disabled in session config
- Suggested solution: Re-enable `touch: true` in session configuration
- Also recommended: Update token refresh to explicitly update Redis TTL

**Session 2 (2024-11-08):**
- Implemented fix in auth.js
- Added unit tests for session refresh behavior
- ChatGPT reviewed implementation and suggested edge case handling
- Testing shows sessions now properly extend on activity

**Final Review:**
- Code ready for deployment
- Tests passing
- Documentation updated
