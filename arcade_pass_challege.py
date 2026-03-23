# 🕹️ Arcade Day Pass Tracker — Challenge Steps

# 1) Create variables to store:
customer_name = 'Anj'
number_of_passes = 20
tokens_per_pass = 3
price_per_pass = 10.5
tokens_required_per_game = 2
games_available = 4

# 2) Calculate:
total_tokens = number_of_passes * price_per_pass

total_cost = tokens_per_pass * price_per_pass
#    - games available  (use 'floor division' to get a whole number)
games_available = total_tokens // tokens_required_per_game



# 3) Print a summary with:
print("========== Arcade Day Pass Tracker — Challenge Steps ==========")
print("Customer name: ", customer_name)
print("Passes bought: ", number_of_passes)
print("Total tokens: ", total_tokens )
print("Total cost: ", str(total_cost))
print("Games available: ", str(games_available))

