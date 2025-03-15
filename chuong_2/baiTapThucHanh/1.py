import numpy as np
import matplotlib.pyplot as plt

def hexagon(center, size):
    """Tạo một hình lục giác dựa trên tâm và kích thước."""
    angles = np.linspace(0, 2 * np.pi, 7)
    x_hex = center[0] + size * np.cos(angles)
    y_hex = center[1] + size * np.sin(angles)
    return x_hex, y_hex

def generate_cells(K, R, grid_size=5):
    """Tạo sơ đồ cell và xác định vị trí các cell đồng kênh."""
    D = np.sqrt(3 * K) * R  # Khoảng cách tối thiểu giữa các cell đồng kênh
    cells = []
    cochannel_cells = []
    
    for i in range(-grid_size, grid_size + 1):
        for j in range(-grid_size, grid_size + 1):
            x = R * 3/2 * i
            y = R * np.sqrt(3) * (j + 0.5 * (i % 2))
            cells.append((x, y))
            
            # Xác định cell đồng kênh
            if (i ** 2 + j ** 2) % K == 0:
                cochannel_cells.append((x, y))
    
    return cells, cochannel_cells, D



def plot_cells(K, R, grid_size=7):
    """Vẽ sơ đồ quy hoạch tần số với nhiều cell hơn."""
    cells, cochannel_cells, D = generate_cells(K, R, grid_size)
    
    plt.figure(figsize=(10, 10))
    for cell in cells:
        x_hex, y_hex = hexagon(cell, R)
        plt.plot(x_hex, y_hex, 'k-', alpha=0.5)
    
    for cell in cochannel_cells:
        x_hex, y_hex = hexagon(cell, R)
        plt.fill(x_hex, y_hex, 'red', alpha=0.3, label='Cell đồng kênh' if 'Cell đồng kênh' not in plt.gca().get_legend_handles_labels()[1] else "")
    
    plt.xlim(-grid_size * R * 2, grid_size * R * 2)
    plt.ylim(-grid_size * R * 2, grid_size * R * 2)
    plt.gca().set_aspect('equal')
    plt.title(f'Sơ đồ quy hoạch tần số (K={K}) ')
    plt.legend()
    plt.show()

# Vẽ sơ đồ với nhiều cell hơn cho K=7 và K=12
plot_cells(K=3, R=1.0, grid_size=10)
plot_cells(K=7, R=1.0, grid_size=10)
plot_cells(K=12, R=1.0, grid_size=10)
