# SolidWorks API Collection 🔧

## About Solprov Engineering

**Solprov Engineering (Pty) Ltd** is a South African mechanical engineering consultancy that has established itself as a versatile solutions provider across multiple industrial sectors. With **14 years of combined professional experience**, the company positions itself as a comprehensive "go-to engineering company" that delivers practical solutions with hands-on assistance and complete project management from concept to completion.

### Company Overview

Solprov Engineering operates as a private limited company headquartered in South Africa, specializing in mechanical engineering solutions across **five primary industry sectors**:

- **Mining** (Core focus area)
- **Industrial Manufacturing**
- **Construction**
- **Agriculture**
- **Aviation**

### Qualifications and Certifications

- **ISO 9001 Standards** - All manufacturing and quality control processes
- **South African Institute of Mechanical Engineers** (SAIME) membership
- **South African Quality Institute (SAQI)** membership
- **Factory Acceptance Testing (FAT)** certification capabilities
- **Professional Engineering Credentials** with 14+ years combined experience

### Engineering Capabilities

#### Mechanical Process Engineering
- Conveyor systems (screw, belt, and chain configurations)
- Rotary kiln systems
- Gearboxes and configured drives
- Pneumatic and hydraulic configurations

#### Electrical and Automation
- Control systems design
- Voltage distribution networks (high to low voltage)
- Industrial process automation
- PLC and SCADA systems integration

#### Civil Engineering
- Structural design for bulk materials handling
- Water infrastructure planning (purification and waste treatment)
- Pumping stations design and implementation
- Site infrastructure development

### Service Delivery Methodology

Solprov follows a structured four-phase approach:

1. **Requirements Analysis** - On-site engineering assistance and assessment
2. **Solution Development** - Collaborative design of cost-effective solutions
3. **Manufacturing** - Fabrication to ISO 9001 standards with complete documentation
4. **Implementation** - Installation, commissioning, and quality control certification

### Strategic Partnerships

To overcome resource constraints, Solprov has developed **multiple cooperation agreements** with:
- Contractors and suppliers
- Specialized manufacturers
- Technical support networks
- Partner companies including DomeShelter, Fluid Systems, Treasure, RefcoSpec, and Greene

---

## SolidWorks API Repository Collection

This collection contains **30 repositories** focused on SolidWorks API development, automation, and integration tools. These repositories have been curated from the GitHub `solidworks-api` topic to provide comprehensive resources for SolidWorks development.

### Repository Categories

#### 🔧 Core Development Frameworks
- **[xarial/codestack](./codestack)** - Comprehensive SolidWorks API documentation and examples
- **[xarial/xcad](./xcad)** - Modern CAD development framework
- **[xarial/xcad-examples](./xcad-examples)** - Practical examples for xCAD framework

#### 🚀 Automation Tools
- **[weianweigan/SolidWorksLookup](./SolidWorksLookup)** - Interactive API exploration tool
- **[Glutenberg/swtoolkit](./swtoolkit)** - Python toolkit for SolidWorks automation
- **[weianweigan/SldWorks.TestRunner](./SldWorks.TestRunner)** - Testing framework for SolidWorks applications

#### 🎯 Specialized Applications
- **[weianweigan/DuSwToglTF](./DuSwToglTF)** - Export SolidWorks models to glTF format
- **[Aeroanion/Free-Solidworks-OBJ-Exporter](./Free-Solidworks-OBJ-Exporter)** - OBJ export functionality
- **[deloarts/pyswx](./pyswx)** - Python SolidWorks integration library
- **[ldevillez/pySwTools](./pySwTools)** - Python tools for SolidWorks automation

#### 🛠️ Add-ins and Extensions
- **[weianweigan/PMPageControl](./PMPageControl)** - Property Manager page controls
- **[RoboMechatronics/myCustomCommand](./myCustomCommand)** - Custom command implementation
- **[RoboMechatronics/MyCustomTaskpane](./MyCustomTaskpane)** - Custom task pane development

#### 📊 Analysis and Optimization
- **[asharahmedjaved/L-Bracket-Optimization](./L-Bracket-Optimization)** - CAD optimization algorithms
- **[JamesStonehouse/HVAC-Optimization-MATLAB-Program](./HVAC-Optimization-MATLAB-Program)** - HVAC system optimization
- **[na-trium-144/solid-descriptor](./solid-descriptor)** - Model description and analysis

#### 🎮 Interactive Tools
- **[Aeroanion/MeasureXForm-Solidworks-Macro](./MeasureXForm-Solidworks-Macro)** - Measurement transformation tools
- **[Johanss-on/Assem2DXF](./Assem2DXF)** - Assembly to DXF conversion
- **[EddyAlleman/SWPUC32---Equidistant-Points-on-a-Hemisphere](./SWPUC32---Equidistant-Points-on-a-Hemisphere)** - Geometric point distribution

#### 🏭 Industry-Specific Solutions
- **[trueshail/SPM_Connect](./SPM_Connect)** - Spare parts management system
- **[halaaro/pdmutils](./pdmutils)** - PDM utility tools
- **[calebcapps/Solidworks-Automation](./Solidworks-Automation)** - Manufacturing automation tools

#### 💼 Business Applications
- **[BlueByteSystemsInc/Blue-Byte-Systems-Inc-Help-Center](./Blue-Byte-Systems-Inc-Help-Center)** - Documentation system
- **[vakanksha2002/API-Development](./API-Development)** - API development examples
- **[maisam-fathi/regal-3d-automation](./regal-3d-automation)** - 3D automation solutions
- **[maisam-fathi/solidwork-assistant](./solidwork-assistant)** - SolidWorks assistant tools
- **[maisam-fathi/standard-part-generator](./standard-part-generator)** - Standard parts generation
- **[AltoAuto/AltoAuto](./AltoAuto)** - Automotive automation tools
- **[AngDan93/Rotation](./Rotation)** - Rotation analysis tools

### Getting Started

1. **Browse the repositories** - Each folder contains a complete SolidWorks API project
2. **Read individual READMEs** - Most repositories include detailed documentation
3. **Check requirements** - Some projects may require specific SolidWorks versions or additional dependencies
4. **Follow installation guides** - Refer to each project's installation instructions

### Development Environment Setup

#### Prerequisites
- **SolidWorks 2016+** (version requirements vary by project)
- **Visual Studio 2019+** or **Visual Studio Code**
- **.NET Framework 4.6+** or **.NET Core 3.1+**
- **Python 3.7+** (for Python-based tools)

#### Common Development Patterns
```csharp
// SolidWorks API Connection Example
SldWorks swApp = (SldWorks)Marshal.GetActiveObject("SldWorks.Application");
ModelDoc2 swModel = (ModelDoc2)swApp.ActiveDoc;
```

```python
# Python SolidWorks Integration
import pythoncom
import win32com.client as win32

sw = win32.Dispatch("SldWorks.Application")
sw.Visible = True
```

### Repository Statistics
- **Total Repositories**: 30
- **Languages**: C#, Python, VB.NET, MATLAB
- **Primary Focus**: SolidWorks API automation and integration
- **License Types**: MIT, Apache 2.0, GPL, Custom licenses

### Contributing

This is a curated collection of existing repositories. To contribute:
1. Fork the original repositories you want to modify
2. Submit improvements to the original maintainers
3. Report issues in respective repository issue trackers

### Support and Resources

- **SolidWorks API Documentation**: [SolidWorks API Help](https://help.solidworks.com/api/)
- **Community Forums**: [SolidWorks API Forum](https://forum.solidworks.com/community/api)
- **Training Resources**: Many repositories include comprehensive examples and tutorials

---

## Collection Maintenance

**Last Updated**: August 2025  
**Repository Count**: 30 active repositories  
**Collection Status**: Complete and ready for development

### Solprov Engineering Contact
For engineering consulting services and SolidWorks integration projects:
- **Company**: Solprov Engineering (Pty) Ltd
- **Location**: South Africa
- **Specialization**: Multi-industry mechanical engineering solutions
- **Certifications**: ISO 9001, SAIME, SAQI certified

---

*This collection serves as a comprehensive resource for SolidWorks API development, backed by Solprov Engineering's expertise in industrial automation and mechanical engineering solutions.*