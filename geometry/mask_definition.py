import numpy as np

def mask_definition() -> np.ndarray:
    scale_factor = 0.045

    vertices_list1 = [(11.0, 11.5), (17.0, 11.5), (17.0, 13.5), (11.0, 13.5)]
    vertices_list2 = [(17.0, 23.0), (19.0, 23.0), (19.0, 11.5), (17.0, 11.5)]
    vertices_list3 = [(11.0, 3.5), (19.0, 3.5), (19.0, 5.5), (11.0, 5.5)]
    vertices_list4 = [(11.0, 7.5), (19.0, 7.5), (19.0, 9.5), (11.0, 9.5)]
    vertices_list5 = [(6.75, 23.0), (9.0, 23.0), (9.0, 3.5), (6.75, 3.5)]
    vertices_list6 = [(9.0, 23.0), (15.0, 23.0), (15.0, 21.0), (9.0, 21.0)]
    vertices_list7 = [(21.0, 23.0), (23.0, 23.0), (23.0, 3.5), (21.0, 3.5)]

    vertices_list1 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list1]
    vertices_list2 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list2]
    vertices_list3 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list3]
    vertices_list4 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list4]
    vertices_list5 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list5]
    vertices_list6 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list6]
    vertices_list7 = [(x * scale_factor, y * scale_factor) for x, y in vertices_list7]

    polygons = [
        (np.array(vertices_list1, dtype=float), "opaque"),
        (np.array(vertices_list2, dtype=float), "opaque"),
        (np.array(vertices_list3, dtype=float), "opaque"),
        (np.array(vertices_list4, dtype=float), "opaque"),
        (np.array(vertices_list5, dtype=float), "opaque"),
        (np.array(vertices_list6, dtype=float), "opaque"),
        (np.array(vertices_list7, dtype=float), "opaque")
    ]
    
    return polygons