# SANS 10131:2004 Tank Design System

## Overview

This repository includes a comprehensive tank design system based on South African National Standard SANS 10131:2004 for above-ground petroleum storage tanks. The system has been developed following Solprov Engineering's quality standards and professional engineering practices.

## Tank Specifications

### Design Standards Compliance
- **Primary Standard:** SANS 10131:2004 - "Above-ground storage tanks for petroleum products"
- **Referenced Design Code:** API 650 - "Welded Steel Tanks for Oil Storage"
- **Quality Standard:** ISO 9001 manufacturing and quality control processes
- **Professional Compliance:** SAIME and SAQI standards

### Tank Design Parameters

#### Main Specifications
- **Capacity:** 9,000 L (9 m³) - Standard BTA (Bulk to Agriculture) tank
- **Type:** Horizontal, cylindrical, shop-fabricated, above-ground storage tank
- **Operating Pressure:** Atmospheric pressure service
- **Design Temperature:** Up to 60°C (140°F)

#### Dimensions
- **Diameter:** 1,870 mm
- **Length (Tan-to-Tan):** 3,680 mm
- **Shell Thickness:** 6 mm (minimum safe thickness for atmospheric service)
- **Overall Length:** ~4,000 mm (including dished ends)

#### Material Specifications
- **Shell & Ends:** Carbon Steel Plate, Grade 300WA per SANS 1431
- **Pipes & Fittings:** Carbon Steel per SANS 62-1
- **Welding Consumables:** Per SANS 9956-3 requirements
- **Fasteners:** Stainless steel or galvanized carbon steel

### Construction Details

#### Tank Ends (SANS 10131:2004 Annex A.3.2.4)
- **Type:** Dished (ellipsoidal) ends
- **Knuckle Radius:** 60 mm (minimum 50 mm required)
- **Crown Radius:** 1,870 mm (equal to tank diameter)
- **Straight Flange:** 40 mm minimum

#### Manhole Assembly (SANS 10131:2004 Annex A.3.4)
- **Diameter:** 600 mm (standard access size)
- **Location:** Centrally positioned on tank top
- **Neck Height:** 100 mm
- **Flange:** 750 mm OD × 20 mm thick
- **Reinforcing Plate:** 800 mm OD × 8 mm thick
- **Cover:** Removable with gasket seal

#### Support System (SANS 10131:2004 Figure A.6)
- **Type:** Two saddle supports
- **Saddle Width:** 250 mm
- **Saddle Height:** 600 mm
- **Contact Angle:** 120° (optimal load distribution)
- **Spacing:** 2,140 mm center-to-center
- **Doubling Plates:** 10 mm thick reinforcement under saddles

#### Lifting System (SANS 10131:2004 Figure A.5)
- **Type:** Two lifting lugs on tank top
- **Dimensions:** 150 mm × 90 mm × 12 mm thick
- **Hole Size:** 50 mm diameter for shackles
- **Capacity:** Suitable for empty tank handling
- **Position:** 2/3 tank length spacing for balance

### Nozzle Configuration

#### Fill Connection
- **Size:** 80 mm (3") nominal diameter
- **Location:** Top of tank, offset from manhole
- **Type:** Flanged connection per SANS standards
- **Purpose:** Product filling operations

#### Vent Connection
- **Size:** 50 mm (2") nominal diameter
- **Location:** Highest point of tank
- **Compliance:** SANS 10131:2004 clause 6.1 venting requirements
- **Function:** Normal and emergency venting per API 2000

#### Product Outlet
- **Size:** 50 mm (2") nominal diameter
- **Location:** Tank end, positioned for complete drainage
- **Height:** 150 mm above tank bottom
- **Type:** Flanged connection with isolation capability

#### Drain Connection
- **Size:** 25 mm (1") nominal diameter
- **Location:** Lowest point of tank bottom
- **Purpose:** Tank cleaning and maintenance drainage
- **Valve:** Required isolation valve

### Safety and Compliance Features

#### Fire Safety (SANS 10131:2004 Section 5)
- **Emergency Venting:** Sized per API 2000 for fire exposure
- **Fire-Fighting Access:** Compliant with local fire authority requirements
- **Safety Distances:** Per SANS 10131:2004 Tables 1, 2, and 3
- **Fire Resistance:** 4-hour rating where required

#### Bunding Requirements (SANS 10131:2004 Section 4)
- **Bund Capacity:** Minimum 110% of tank volume
- **Wall Height:** Sufficient for required volume plus freeboard
- **Drainage:** Controlled drainage system with manual operation
- **Construction:** Reinforced concrete or equivalent

#### Environmental Protection
- **Corrosion Protection:** Sa 2½ blast cleaning per ISO 8501-1
- **Coating System:** Primer and topcoat for petroleum service
- **Cathodic Protection:** As required for buried components
- **Leak Detection:** Visual inspection capability

### Quality Assurance Program

#### Manufacturing Standards
- **Quality Management:** ISO 9001 certified processes
- **Welding Standards:** SANS 9956-3 procedures
- **Welder Qualification:** SANS 9606-1 certification required
- **Material Certification:** Mill test certificates required

#### Testing and Inspection
- **Visual Inspection:** 100% of all welds
- **Pressure Testing:** Hydrostatic test per Annex A.4
- **Non-Destructive Testing:** Radiographic testing of critical welds
- **Documentation:** Complete quality records package

#### Factory Acceptance Testing (FAT)
- **Hydrostatic Test:** 1.5 × design pressure minimum
- **Leak Test:** Soap solution or equivalent
- **Dimensional Verification:** All critical dimensions checked
- **Certificate:** FAT certificate issued upon completion

### Installation Requirements

#### Foundation
- **Type:** Reinforced concrete pad or ring wall
- **Level:** ±3 mm over tank length
- **Drainage:** Positive drainage away from tank
- **Access:** Vehicle access for delivery and maintenance

#### Piping Connections
- **Flexibility:** Adequate for thermal expansion
- **Support:** Independent of tank structure
- **Isolation:** Valves for each connection
- **Labeling:** Clear identification of all connections

#### Commissioning
- **System Testing:** Complete system pressure test
- **Calibration:** Level indication and alarms
- **Documentation:** As-built drawings and operating manual
- **Training:** Operator training program

## Usage Instructions

### Running the Tank Generator

1. **Install Dependencies:**
   ```bash
   pip install build123d
   ```

2. **Run the Generator:**
   ```bash
   python tank_design_generator.py
   ```

3. **Generated Files:**
   - `SANS_10131_10000L_Tank.stp` - 3D model for SolidWorks
   - `tank_design_documentation.md` - Detailed specifications

### Opening in SolidWorks

1. Launch SolidWorks
2. File → Open → Select the `.stp` file
3. Import the model with default settings
4. The tank will appear as a complete assembly

### Customization Options

The `tank_design_generator.py` script can be modified to adjust:
- Tank capacity and dimensions
- Shell thickness for different pressures
- Nozzle sizes and positions
- Support configurations
- Material specifications

## Professional Services

### Solprov Engineering Capabilities

**Company:** Solprov Engineering (Pty) Ltd  
**Certifications:** ISO 9001, SAIME, SAQI  
**Experience:** 14+ years combined professional experience

#### Engineering Services
- **Design & Analysis:** Pressure vessel design per SANS and API standards
- **Manufacturing:** ISO 9001 certified fabrication processes
- **Installation:** Complete project management from concept to commissioning
- **Maintenance:** Preventative and predictive maintenance programs

#### Multi-Industry Expertise
- **Mining:** Bulk materials handling, process systems
- **Industrial:** Manufacturing automation, quality systems
- **Construction:** Structural design, infrastructure
- **Agriculture:** Storage and processing systems
- **Aviation:** Specialized engineering solutions

#### Quality Management
- **Standards Compliance:** SANS, API, ASME, ISO standards
- **Professional Oversight:** Licensed professional engineers
- **Quality Control:** Comprehensive testing and inspection
- **Documentation:** Complete project documentation packages

### Technical Support

For technical questions about tank designs or modifications:
- Review SANS 10131:2004 standard requirements
- Consult with qualified professional engineers
- Ensure compliance with local regulations
- Obtain appropriate certifications and approvals

### Regulatory Compliance

Before installation, ensure compliance with:
- **Municipal bylaws** - Local authority approvals
- **Environmental regulations** - Impact assessments
- **Fire authority requirements** - Safety clearances
- **Insurance requirements** - Risk assessments
- **Occupational health and safety** - Workplace safety

## Integration with SolidWorks API Collection

This tank design system integrates with the broader SolidWorks API collection by:
- Providing practical engineering examples
- Demonstrating professional standards compliance
- Showing real-world application of CAD automation
- Supporting multi-industry engineering solutions

The tank generator serves as an example of how SolidWorks API tools can be used to create standardized, compliant engineering solutions that meet professional quality standards.

---

**Disclaimer:** This tank design system is provided for educational and reference purposes. All designs must be reviewed by qualified professional engineers and comply with local regulations before construction or installation. Solprov Engineering (Pty) Ltd accepts no responsibility for designs not professionally reviewed and approved.