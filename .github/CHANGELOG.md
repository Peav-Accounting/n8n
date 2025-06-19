# Changelog

## [Agent Feedback System & Test B1 Eval Harness] - 2025-06-11

### Added
- New workflow `test-B1.json` for processing bookkeeping entries from CSV
- Test case `B1/test_case_001.json` to validate missing description handling
- Eval runner script to execute and validate test cases
- Automated feedback loop for agent performance monitoring
- New webhook workflow for capturing agent feedback and errors
- GitHub feedback logger script to store errors in repository
- Test payload for webhook validation
- Integration with GitHub API for error logging

### Technical Details
- Webhook accepts POST requests with agent_id, error_type, and message
- Python script interfaces with GitHub API to update error logs
- Error data stored in .github/feedback/agent_errors.json
- Includes error context and timestamps for debugging
>>>>>>> master
