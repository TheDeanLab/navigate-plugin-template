<h1 align="center">
<img src="https://github.com/TheDeanLab/navigate-plugin-template/blob/main/plugin-icon.jpg" width="200" height="200"/>

navigate-plugin-template
	
<h2 align="center">
	A Template for Creating Plugins for navigate
</h2>
</h1>

The **navigate-plugin-template** is a starter kit for developers looking to create plugins for the **navigate** light-sheet microscope control software. This template provides a basic structure and guidelines to help you develop and integrate new plugins into **navigate**. 

More information on how to develop your own plugins can be found [here](https://thedeanlab.github.io/navigate/advanced.html).

### Getting Started

1. **Fork this Repository**: Click the 'Fork' button at the top of this page to create your own copy of this template.
2. **Clone your Fork**: Clone your forked repository to your local machine.
3. **Create a New Branch**: It's a good practice to create a new branch for your plugin development.
4. **Develop Your Plugin**: Use the template structure to develop your plugin. Make sure to follow the guidelines provided in the `CONTRIBUTING.md` file.
5. **Test Your Plugin**: Ensure your plugin works as expected with Navigate.

### Template Structure
Both navigate, and the navigate-plugin-template, are organized in an industry-standard Model-View-Controller architecture. 

- `model/devices/`: Device communication protocols for your plugin. Enables you to add new devices and extend the functionality of **navigate**.
- `model/features/`: A feature template for your plugin. Enables you to use it as part of `smart` imaging workflows.
- `view/`: Graphical user interface for your plugin. 
- `controller/`: Sub-controller for your plugin, which coordinates actions placed in the graphical user interface with device control. 

### Contributing

After developing your plugin, you can contribute it back to the Navigate community. Please see our contribution guidelines for more information.

### Support

For support or questions about using this template, please open an issue in the GitHub repository.

### License

This template is open source and available under the same license as Navigate.
