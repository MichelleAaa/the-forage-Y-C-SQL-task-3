From: The Forage - Y-C - Task 3
 

<h2 id="task"> Module 3 Task Overview </h2>
<p>Analytics - Analyse the latest feature releases</p>
<p> <b>Aim:</b>Create insights and ideas backed by data</p>

<p>Please clone this repository to start the task. Edit file <b>answer.sql</b> with your SQL query to produce meaningful data</p>

<p>On 2018-06-02, we released the Kanban Board on Shiptivity app. It has a major impact on our stats and we want to iterate on it</p>

<b>Purpose</b>
<p>We want to generate a few key ideas to move us on one of our core metrics: daily active users.</p>

<b>Acceptance Criteria</b>
<ol>
<li>This task is complete when we have a graph created that maps out the daily average users before and after the feature change</li>
<li>This task is complete when we have a graph of the number of status changes by card</li>
<li>This task is complete when you upload the SQL queries that can generate this information</li>
<li>This task is complete when we have three actionable ideas stated in the format below:
<ol>
	<li>Hypothesis </li>
	<li>Expected Impact </li>
	<li>What the feature is (a quick explanation of the feature)</li>
</ol>
</li>
<li>Sketches and flows of these features are optional but helpful (wireframe quality is enough)</li>
</ol>

<h2 id="installation" >Installation</h2>

<p>
You will need to have <b>sqlite3</b> installed

If you do not have sqlite3 installed, follow this <a href="https://www.tutorialspoint.com/sqlite/sqlite_installation.htm">guide</a> on how to install sqlite3.

On your terminal, try running <code>sqlite3 ./shiptivity.db</code>.

You can start running SQL command on the terminal.
</p>
<p>Tips: try <code>.schema</code> to see a list of CREATE TABLE commands for the db.</p>

<p> If you want to go back to tthe original state of db, there is a <code>dump</code> called shiptivity.dump that you can run to restore the data to its unchanged state.
