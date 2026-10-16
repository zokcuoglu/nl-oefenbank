/**
 * Google Apps Script: starts the GitHub "Mailer" workflow every hour.
 *
 * Why: GitHub's own hourly schedule (cron in .github/workflows/mailer.yml) is not reliable;
 * it often skips hours. Apps Script time triggers run on time, so this script asks GitHub
 * to start the workflow. Both can stay on: the mailer keeps logs, so nothing is sent twice.
 *
 * Setup (once):
 * 1. GitHub > Settings > Developer settings > Fine-grained tokens > Generate new token
 *    - Repository access: Only select repositories > nl-oefenbank
 *    - Permissions > Actions: Read and write (nothing else)
 * 2. script.google.com > New project > paste this file.
 * 3. Project settings (gear) > Script properties > add GITHUB_TOKEN = the token from step 1.
 *    (Keep the token out of the code: the code may be shared, the properties are private.)
 * 4. Run triggerMailer once by hand and allow the permissions; check Actions in GitHub for a new run.
 * 5. Triggers (clock icon) > Add trigger > triggerMailer > Time-driven > Hour timer > Every hour.
 */
function triggerMailer() {
  var token = PropertiesService.getScriptProperties().getProperty('GITHUB_TOKEN');
  if (!token) throw new Error('Script property GITHUB_TOKEN is missing (see setup step 3).');

  var url = 'https://api.github.com/repos/zokcuoglu/nl-oefenbank/actions/workflows/mailer.yml/dispatches';
  var res = UrlFetchApp.fetch(url, {
    method: 'post',
    contentType: 'application/json',
    headers: { Authorization: 'Bearer ' + token, Accept: 'application/vnd.github+json' },
    // mode "hourly" = the normal run; dry_run must be false, otherwise it only prints
    payload: JSON.stringify({ ref: 'main', inputs: { mode: 'hourly', dry_run: 'false' } }),
    muteHttpExceptions: true
  });

  // GitHub answers 204 (no content) when the run was started
  if (res.getResponseCode() !== 204) {
    throw new Error('GitHub answered ' + res.getResponseCode() + ': ' + res.getContentText());
  }
}
