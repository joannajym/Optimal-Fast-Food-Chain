# Optimal Fast Food Chain

## Project Overview
This project focuses on assisting a fast food chain company in strategically selecting sites along a newly built freeway to open new restaurants. The primary goal is to maximise overall revenue while adhering to the company's policy that no two restaurants can be within 'd' kilometers of each other. The challenge is tackled by developing a Python function 'restaurantFinder(d, site_list)', which employs a dynamic programming approach to ensure optimal site selection with O(N) time and space complexity

## Example usage
d = 2

site_list = [3, 2, 3, 4, 1, 2]

total_revenue, selected_sites = restaurantFinder(d, site_list)

print("Total Revenue:", total_revenue)

print("Selected Sites:", selected_sites)
