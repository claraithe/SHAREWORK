# Work Item Example: Code Optimization

## Work Item: Optimize Database Query Performance

**Priority**: High  
**Status**: In Progress  
**Created**: 2024-11-08  
**Assigned to**: ChatGPT

---

### Description
Optimize the customer data retrieval queries that are currently causing slow page load times in the dashboard. The main issue is with the `getUserOrders` function which retrieves order history.

---

### Context
- Current query takes 3-5 seconds to load for users with many orders
- Using PostgreSQL database
- Application is built with Node.js and Express
- 10,000+ active users
- Some users have 1000+ orders in the system
- No current indexing strategy on the orders table

---

### Tasks
- [x] Analyze current query structure
- [x] Identify bottlenecks using EXPLAIN ANALYZE
- [ ] Design optimal indexing strategy
- [ ] Implement query optimization
- [ ] Test performance improvements
- [ ] Update documentation

---

### Expected Outcome
- Query execution time reduced to under 500ms
- Page load time improved by at least 60%
- No breaking changes to existing API
- Proper indexes created on orders table
- Documentation updated with performance notes

---

### Resources
- **Files**: 
  - `src/controllers/userController.js`
  - `src/models/Order.js`
  - `database/schema.sql`
- **Documentation**: 
  - PostgreSQL Performance Tuning Guide
  - Current API documentation
- **References**: 
  - User feedback ticket #1234
  - Performance monitoring dashboard

---

### Notes
- Peak usage hours: 9 AM - 5 PM EST
- Need to test on staging before production deployment
- Consider implementing caching strategy for frequently accessed data

---

### ChatGPT Collaboration Notes

**Session 1 (2024-11-08):**
- Analyzed current query structure
- ChatGPT suggested adding composite index on (user_id, created_at)
- Recommended implementing pagination for large result sets
- Suggested using query result caching with Redis

**Next Steps:**
- Implement suggested indexes
- Add pagination to API endpoint
- Evaluate Redis caching solution
