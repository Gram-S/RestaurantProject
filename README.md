Testing creating a new branch. This will be the branch for the first sprint. 

What i have done here is created the basic restaurant models in models.py

MenuItem: what its for
    Servers choose these items when creating orders
    Managers can edit the menu
    the kitchen sees these items on tickets

SubstitutionOption
allows for substitutions ("add cheese, switch side dish, gluten free etc.")


Order
One order per table per customer
server is who requested the order
status is its current status
created at shows times it was put in to the kitchen (for manager tracking or whatever)

OrderItem
A single order for a table may need multiple items
this stores each one and its notes for the kitchen if any. 

Ive added code stubs for views for the kitchen, manager, and server and what I think we could reasonably do before tuesday but feel free to go wild

I also added some very very basic HTML templates and set up URL routing for the views once they are done. 

I tried to set up the structure here for ease of splitting the three sides we have essentially, server, kitchen, manager into their owns sections for everything to keep the code clean. 

Let me know if I goofed anything or something is dumb. 

I think if we get this done, we are already mostly done its just polishing up workflow and adding little features here and there so the rest of the sprints should be good. 