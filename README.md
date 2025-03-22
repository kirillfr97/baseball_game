# Baseball

## Objective/Problem:

You need to design a simplistic baseball game simulation.

There should be a 9-inning game between 2 teams, the **"red"** team and the **"blue"** team.

There is a standard baseball diamond with **1st, 2nd, and 3rd bases, and a home plate**. All batters that get a hit and make it back to home plate score a run.

A batter can **strike out**, or get a **single, double, triple, or home run**. Each batter's turn is decided by generating a random number between **1 and 8**, which dictates their action as follows:

- **1** – Go to 1st base. All other players on base advance one base.  
  *(i.e. 1st goes to 2nd, 2nd to 3rd, 3rd to home and scores a run)*
- **2** – Go to 2nd base. All other players on base advance two bases.  
  *(i.e. 1st goes to 3rd, 2nd and 3rd go home and score runs)*
- **3** – Go to 3rd base. All other players on base advance three bases.  
  *(i.e. all players already on base go home and score runs)*
- **4** – Home Run. Batter and all players on base score runs.
- **5-8** – Out.

To keep things simple, we assume that any runners on base all advance at the same rate. That is:

- If a **single** is hit, all runners advance **1 base**. *(There is no base stealing.)*
- If a **double** is hit, all runners advance **2 bases**.
- If a **triple** is hit, all runners advance **3 bases**.
- If a **home run** is hit, then all runners advance to **home plate**.

The program should print messages showing the flow of the game, including:

- When each team is at bat.
- The results of each batter.
- When runs are scored (along with how many).

---

## Question:

How would you store the base position of the runners, and how would you manage advancing bases and keeping track of runs scored?

### Specifically, create a `Bases` class that will be used to manage the bases, and add a constructor and at least two methods:

- `advance_bases(number_of_bases_to_advance)`
- `calculate_new_runs()`

### Hint:  
You should look for a solution that is **efficient in both memory usage and execution time**.
