import SimpleITK as sitk
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

def visualize_segmentation_slice_greybg_label0grey(image_path, segmentation_path, output_path, slice_index=None, orientation='axial', segmentation_colormap='viridis', bg_color='gray'):

    try:
        # Read the image and segmentation using SimpleITK
        image_sitk = sitk.ReadImage(image_path)
        segmentation_sitk = sitk.ReadImage(segmentation_path)

        # Convert SimpleITK images to NumPy arrays
        image_np = sitk.GetArrayFromImage(image_sitk)
        segmentation_np = sitk.GetArrayFromImage(segmentation_sitk)

        # Determine slice index if not provided
        if slice_index is None:
            if orientation == 'axial':
                slice_index = image_np.shape[0] // 2
            elif orientation == 'coronal':
                slice_index = image_np.shape[1] // 2
            elif orientation == 'sagittal':
                slice_index = image_np.shape[2] // 2
            else:
                raise ValueError("Invalid orientation. Choose from 'axial', 'coronal', 'sagittal'.")

        # Extract slice based on orientation
        if orientation == 'axial':
            image_slice = image_np[slice_index, :, :]
            segmentation_slice = segmentation_np[slice_index, :, :]
        elif orientation == 'coronal':
            image_slice = image_np[:, slice_index, :]
            segmentation_slice = segmentation_np[:, slice_index, :]
        elif orientation == 'sagittal':
            image_slice = image_np[:, :, slice_index]
            segmentation_slice = segmentation_np[:, :, slice_index]

        # Create custom colormap for segmentation
        base_cmap = plt.cm.get_cmap(segmentation_colormap) # Get the original colormap (e.g., 'viridis')
        colors = base_cmap(np.linspace(0, 1, 4)) # Extract 4 colors from it
        colors[0] = [0.5, 0.5, 0.5, 1] # Set the first color (index 0) to grey (RGBA: [0.5, 0.5, 0.5, 1])
        custom_seg_cmap = ListedColormap(colors) # Create a ListedColormap from these colors


        # Create the visualization
        plt.figure(figsize=(10, 10)) # Adjust figure size as needed

        # Display the image slice in specified background color (default: grey)
        plt.imshow(image_slice, cmap=bg_color) # Set colormap for the image here

        # Overlay the segmentation with the *custom* colormap and transparency
        plt.imshow(segmentation_slice, cmap=custom_seg_cmap, alpha=0.5, vmin=0, vmax=3) # Assuming labels 0, 1, 2, 3

        # Add colorbar for segmentation labels (optional)
        plt.colorbar(ticks=[ 0, 1, 2, 3], label='Segmentation Labels') # Adjust ticks if your labels are different
        colorbar = plt.gca().images[-1].colorbar # Get the colorbar object
        colorbar.set_ticks([0, 1, 2, 3]) # Ensure ticks are still at 0, 1, 2, 3
        colorbar.set_ticklabels(['0 (Grey)', '1', '2', '3']) # Update tick labels to indicate 0 is grey

        # Set title and axis labels (optional)
        plt.title(f'{orientation.capitalize()} Slice {slice_index}')
        plt.xlabel('Pixel Column')
        plt.ylabel('Pixel Row')
        plt.xticks([]) # Remove x axis ticks
        plt.yticks([]) # Remove y axis ticks

        # Save the visualization as a PNG file
        plt.savefig(output_path)
        plt.close() # Close the figure to free memory

        print(f"Visualization saved to: {output_path}")

    except Exception as e:
        print(f"Error during visualization: {e}")

