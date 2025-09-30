# Designed and built my first 3NF database

#### 21st September 2025

### What?

On 21st of September 2025, I have created my first-ever 3NF database schema. 

I got back to working on an application that I had begun and abandoned about a year ago. The application is an electronic journal where the user can submit entries and track their activity and progress over time.

When I had returned to the application, the biggest problem I identified was the database. It was an unnormalized form (UNF). It had one field that was not atomic - "Activities". It had duplicates, most notably the "Mood" field, which was an independent field in 2 separate tables (unconstrained by relationship). The "Activities" table could hold duplicate records. 



'What?' helps you describe the situation you want to learn from. You should identify the facts and feelings of the situation.

### So what?

'So What?' allows you to extract the meaning of 'What?'. Moreover, you should question what knowledge you and others had in the situation, and what knowledge or theories that could help you make sense of the situation.

### Now what?

'Now what?' allows you to create an action plan for the future based on the previous questions.
