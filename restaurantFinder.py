def restaurantFinder(d, site_list):
    """
    Function description: Function that calculates the maximum total revenue possible by selecting sites from a given list based on the minimum distance between
    any two selected sites 'd', and a list of potential revenue values for each site 'site_list'. 

    Approach description: First is the initialization step, where we initialise 'count' to determine the number of sites and the DP arrays, where 'total_revenue[i]'
    will store the maximum revenue obtained considering the first i+1 sites, and 'last_selected' will help in backtracking the sites that were selected.
    If d = 0 and the total revenue from all sites is negative, then it's optimal to not select any sites.

    The function then enters a DP loop that iterates through each site in the 'site_list' and makes the best decision for each site based on the estimated revenue
    from the previous sites. 'select_revenue' will be the revenue if site i is selected. So if site i is selected, we will also add the revenue from the best selection 
    that excludes the next d sites. For the first site when i = 0, the maximum revenue is either 0 (site is not selected) or the site's revenue if it's positive.
    For subsequent sites, the decision is between not selecting site i and taking the maximum revenue from the previous site, or selecting the site i and adding its
    revenue to the best revenue from the sites before the distance constraint.

    The algorithm then backtracks the selected sites based on the results from the DP solution. It first checks which sites were selected, starting from the last site 
    and moving backward. If site i was selected, it's added to selected_sites. The code skips d sites and continues backtracking due to the distance constraint.
    
    The function then returns two values: the maximum revenue possible, and the list of selected sites.


    Given that N is the number of sites in site_list:

    The time complexity of this algorithm is O(N) since it calculates the sum of the entire site_list once, and that the main loop goes through each of the N sites
    once. Additionally the backtracking process iterates through each on the N sites once at worst case O(N) time.

    The auxiliary space complexity is O(N) since we use two auxiliary lists of size N to store the values and backtracking information for each of the N sites.

    :Input:
        d (int): Represents the minimum number of miles between any two selected sites.
        site_list (List[int]): List of integers where each integer represents the annual revenue that a Burger Queen restaurant would generate if it were places at a
        particular site.

    :Output: Returns a tuple with two elements: the best possible annual revenue attainable and the sites that need to be chosen to achieve this revenue.

    :Time complexity: O(N), where N is the number of sites.

    :Aux space complexity: O(N), where N is the number of sites.
    """
    count = len(site_list)  # Initialises count to hold total number of sites containing potential revenue values

    # Create arrays to hold our DP results and to backtrack
    total_revenue = [0] * count
    last_selected = [-1] * count
    
    # Case that checks if d = 0 and sum of all revenues is negative
    if d == 0 and sum(site_list) <= 0:
        # No sites chosen to maximise revenue
        return 0, []
    
    # Iterates through each site to calculate the max revenue when i-th site is considered
    for i in range(count):
        select_revenue = site_list[i]   # Initializes revenue for current site i
        
        # Checks if it's possible to choose the previous site such that d is maintained
        if i - d - 1 >= 0:
            # Adds total revenue from the previous site to select_revenue
            select_revenue += total_revenue[i-d-1]
        
        # Base case for the very first site
        # Checks if the revenue for this site is positive. If it is, site is chosen; otherwise, revenue is set to 0
        if i == 0:
            total_revenue[i] = max(0, site_list[i])
            if site_list[i] > 0:
                last_selected[i] = i

        else:
            # Checks if total revenue from not selecting current site is greater than revenue of selecting it
            if total_revenue[i-1] > select_revenue:
                # Total_revenue for current site i remains the same as the previous site
                total_revenue[i] = total_revenue[i-1]
            
            # Else, current site is selected
            else:
                total_revenue[i] = select_revenue
                last_selected[i] = i    # Current site marked as selected in last_selected list
    
    # Backtrack to get the list of selected sites
    selected_sites = []     # Initialises empty list to store list of selected restaurant sites
    i = count - 1   # Initialises i to the last site considered

    # Iterates backwards from last site to the first
    while i >= 0:
        # Checks if the site at index i was selected
        if last_selected[i] != -1:
            selected_sites.append(last_selected[i] + 1) # If site was selected, its index is added to selected_sites list
            i = i - d - 1   # Jumps to d+1 positions earlier in the list
        else:
            i -= 1  # If current site at i was not selected, move one position backward to previous site
        
    selected_sites.reverse()    # Reverse selected_sites to get correct order of selected sites

    # Returns maximum revenue possible and list of selected sites
    return total_revenue[-1], selected_sites
