# Using BragLog
BragLog helps you maintain a record of your professional achievements. This guide covers all essential commands for managing your accomplishments, from adding new entries to generating reports for performance reviews.

## Adding Work Achievements

To log today's achievement:
```bash
braglog Fixed the authentication bug in login module
```

To log an achievement for a specific date:
```bash
braglog "Completed code review for PR #123" --date 2025-03-19 
```

To see the location of your logs file:
```bash
braglog logs-path
```
## Viewing Work Achievements

View all entries or filter them:
```bash
# Show all entries
braglog show

# Filter by text
braglog show --contains "bug fix"

# Show entries for specific date
braglog show --on "2025-03-19"

# Quick manager meeting prep - show last 2 weeks of achievements
braglog show -s "2 weeks ago"
```
> [!NOTE]
> `--on` cannot be used with `--since` or `--until`
## Delete Achievements

For deleting records, simply use `--delete`:
```bash
braglog show --on today --delete
```

## Editing Achievements

To edit existing entries interactively:
```bash
# Edit all entries
braglog show --edit
```
> **NOTE**: The editor used is determined by your `EDITOR` environment variable (typically vim, nano, etc)
