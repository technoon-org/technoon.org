---
title: AINoon Tutorial 3
---

The goal of this tutorial is to **make your own agent to come up with
movie-themed dessert ideas for a restaurant.**

We'll use Zapier, a website for automating workflows, which makes it
easy to build AI agents.


## Set up a table to store the ideas

1. Open [zapier.com](https://zapier.com)
2. Open **Tables** from the sidebar
   * It's possible to integrate Zapier to work with tables and
     spreadsheets in other systems
   * But we'll using a table in Zapier itself so that we don't have to
     set up any integrations
3. Click the **Create** button
4. Select **Blank table**
5. Name the table **Dessert ideas**
6. We now see an empty table with no fields/columns

There's a **Copilot** on the left side of the screen - an agent Zapier
has provided to help us set up a table.

Let's ask it to add the fields we need:

```
Add fields for the name, movie, and description for each dessert idea
```

* Notice how it "thought for a moment"
  * This is *chain-of-thought* or *reasoning*
  * You can click the dropdown to see what it said to itself
* The copilot will ask you to confirm the fields its going to add
  * Note how it says its using a tool to add the fields!

You should now see three fields:

1. Name (text)
2. Movie (text)
3. Description (long text)

* If you see those columns your table is ready to go!
* Otherwise add them or change the field types manually
  * *Demonstrate this if anyone had issues with the copilot*
  * *In particular, it often seems to add the requested columns twice*


## Create the agent

1. In a new tab, open [zapier.com](https://zapier.com) again
2. Open **Agents** from the sidebar
3. Click the **New agent** button

Another copilot to help us build our agent! Let's describe what we
want the agent to do, and let the copilot configure it for us:

```
1. Get the top 3 family movies releasing next month
2. For each movie, come up with a fun themed dessert to sell at our restaurant
3. Add each dessert to the "Dessert ideas" Zapier table
```

Again, we can see the copilot's reasoning and tool use:

1. It has set up the instructions based on our description
   * Including a *Final goal*
2. It has added and configured the *Zapier Tables: Create Record*
   * Click on the cog to check the configuration
   * It should have selected the **Dessert ideas** table
   * It should **Let your agent generate a value for this field**
     * Sometimes it sets it to a hard-coded value, so demonstrate how
       to change this if anyone needs to
3. It doesn't need to add a tool for web searching, as that tool is
   always available in Zapier agents
4. It has even given our agent a descriptive name!

We still need to add a trigger - when the agent should run:

1. Click the **Add trigger** button
2. Select **On demand**, so that it will run when we manually trigger it
   * We could have also selected to run it on a schedule
   * Or to be triggered by another system, like email


## Test the agent

1. Click **Agent preview**
2. Click **Test agent**
3. Watch what it does!

You should see it:

1. Perform one or more calls to the *Google Search* or *Web browsing*
   tools to find upcoming family movies
2. Come up with a dessert idea for each movie
3. Use the *Zapier Tables: Create Record* tool to add each dessert to
   your table
   * It will ask you to approve each time it adds a row
4. Provide a summary of its work at the end

Go back to the browser tab of your table, and you should see three
rows have been added!

### **AUDIENCE QUESTION:** How well did your agent do?

* Did it successfully add desserts to the table?
* Did it get movies from the future?
* Do the dessert ideas sound good?
* Did you notice anything else interesting?


## Conclusion

* You've now created an agent *and* used a couple of "copilot" agents
  to help you do it!
* In your own time:
  * Have a look at the list of triggers and tools that Zapier has
    available for integrating with other systems
  * Try refining the agent instructions to further control the kind of
    desserts or movies
  * Try building an agent to automate something of interest to you!
* There is also a homework exercise to extend this agent into a
  "multi-agent" system that uses another agent to generate a recipe
  for each dessert.
