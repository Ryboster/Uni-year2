# Designed and built my first 3NF database

#### 21st September 2025

### What?

On 21st of September 2025, I have created my first-ever 3NF database schema. 

I got back to working on an application that I had begun and abandoned about a year ago. The application is an electronic journal where the user can submit entries and track their activity and progress over time.

When I had returned to the application, the biggest problem I identified was the database. It was an unnormalized form (UNF), and it had many architectural problems.

* It had one field that was not atomic - "Activities" field of "Entries" table. This field held multiple indivisable values.

* The "Activities" table could hold duplicate records because it had no UNIQUE constraints or a primary key. It only had a foreign key associated with a primary key "Category" inside "Categories" table. It was a one-to-many relationship.

* There was no database-enforced relationships between related tables and their fields, e.g. The "Mood" field of the "Entries" table had no association with the "Mood" field from the "Moods" table at the database level. This relationship only existed at the application level, which lead to some undesirable behaviours such as  having to edit both values manually. What a headache!

* 

Since the management system was split between the database level and the application level, it was incredibly difficult to work on the application because it was unclear what change would result in what. Additionally, it also resulted in questionable and inconsistent management, and ultimately patchy, hard to maintain and unreadable code.

The lack of relationships also lead to undesired data being stored. The "Entries" table should be unable to hold a "Mood" value that doesn't exist in the "Moods" table. However, since the two fields weren't related, such a case was allowed. This lead to 

However, since there was no such relationship, such a case was allowed until the right application-level script was triggered and the record was removed.





### So what?

'So What?' allows you to extract the meaning of 'What?'. Moreover, you should question what knowledge you and others had in the situation, and what knowledge or theories that could help you make sense of the situation.

### Now what?

'Now what?' allows you to create an action plan for the future based on the previous questions.
