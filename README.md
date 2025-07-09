# store-path-optimizer

The program uses the map of a generic Walmart supercenter to calculate the shortest possible route that obtains each item in a list, based on its section in the store. It uses the distance formula to get an estimate for the distance between sections, accounting for the ability to walk between them.
### Inputs
* start_entrance: either right or left
* section_list: list of section names (e.g., ["Deli", "Books", "Pharmacy"])

### Map
![walmart store layout](https://github.com/user-attachments/assets/2c481088-b4fc-4c8e-9742-65836a8d3f02)
<sub>*source: https://www.flickr.com/photos/139188400@N08/53807428653*</sub>

### Gridded Map
![grid walmart store layout](https://github.com/user-attachments/assets/e6cbf47f-f847-47bb-ae45-deac0e851b21)
* The x and y axes are located at the bottom and left of the map, respectively
* The grid is based on a unit scale
* Each coordinate location is rounded to an integer point based on the nearest entrance (left or right).

The program first plots the sections of the store as points using matplotlib so the user can visualize their locations and understand valid inputs.
The user inputs their starting entrance and the list of sections needed to visits.

* variables are set
* loops through each section in the list until the list is complete
* uses logic to determine which distances to calculate and uses distance formula for each distance
* finds minimum distance for each remaining section and adds it to the path

The shortest path (based on distance to each nearest remaining section) is then returned.

<sub>*this program could improve runtime and accuracy using Dijkstra's or nearest neighbor algorithms, and a deque data structure may be more efficient. May be improved in the future*
