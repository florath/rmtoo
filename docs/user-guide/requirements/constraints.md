# Requirements vs Constraints

Understanding the difference between requirements and constraints is fundamental to effective requirements management in rmToo.

## Definitions

### Requirements
A requirement is a behavior, action, or characteristic specified by other requirements. Requirements define **what** the system should do.

### Constraints
Constraints are limitations on the solution space of a requirement. They define **how** the system should implement the requirements, or what restrictions apply.

## Key Characteristics

### Requirements
- Define functionality and behavior
- Specify system capabilities
- Are solution-independent
- Form hierarchical relationships through dependencies

### Constraints
- Always associated with one or more requirements
- Limit the possible solutions
- Are (usually) automatically verifiable
- Inherit from parent requirements to dependent requirements

## Inheritance Model

Constraints typically inherit from the directly associated requirement to all dependent requirements. This inheritance model ensures that design decisions and limitations propagate through the entire requirement hierarchy.

## Example: Digital Thermometer

Let's consider designing a digital thermometer that must withstand accelerations of 7G.

### Master Requirement
```
Name: Thermometer
Solved by: Display Housing TemperatureSensor Electronics PowerSupply
Constraints: AccelerationMax7G
```

In this example, the constraint `AccelerationMax7G` inherits to all components (Display, Housing, TemperatureSensor, Electronics, PowerSupply).

### Component with Conflicting Constraint
```
Name: HousingA
Solved by: ...
Constraints: AccelerationMax5G
```

This creates a conflict because:
- The parent requirement requires **7G acceleration resistance**
- This specific housing only supports **5G acceleration resistance**

## Automatic Conflict Detection

One of rmToo's goals is the automatic checking of such constraints and detection of possible conflicts. This helps identify:

1. **Inheritance conflicts**: When child requirements have constraints that conflict with parent requirements
2. **Component incompatibilities**: When existing components don't meet system-level constraints
3. **Design contradictions**: When multiple constraints cannot be satisfied simultaneously

## Practical Usage in rmToo

### Defining Constraints
In rmToo, constraints are typically defined using the `Constraints` field in requirement files:

```
Name: SystemRequirement
Description: The system must meet specific performance criteria
Constraints: 
 - MaxResponseTime2sec
 - MinThroughput100rps
 - MaxMemoryUsage512MB
Solved by: UserInterface DataProcessor NetworkModule
```

### Constraint Verification
rmToo can automatically verify constraints when:
- Constraints are defined in a machine-readable format
- Verification rules are implemented
- Test cases validate constraint compliance

### Constraint Inheritance
When a requirement has constraints, all requirements that solve it inherit these constraints unless explicitly overridden.

## Best Practices

### 1. Clear Constraint Definition
- Use descriptive constraint names
- Document constraint values and units
- Specify measurement criteria

### 2. Hierarchical Constraint Management
- Apply constraints at the appropriate level
- Avoid over-constraining low-level requirements
- Use inheritance to propagate system-level constraints

### 3. Conflict Prevention
- Review constraint inheritance paths
- Check for contradictory constraints early
- Use constraint analysis tools

### 4. Verifiable Constraints
- Make constraints measurable
- Define test procedures
- Automate constraint checking where possible

## Implementation in rmToo

### Current Status
rmToo provides basic constraint support through:
- Constraint fields in requirement files
- Constraint inheritance through requirement dependencies
- Manual constraint conflict detection

### Future Enhancements
Planned improvements include:
- Automatic constraint conflict detection
- Constraint verification automation
- Integration with testing frameworks
- Graphical constraint visualization

## Common Constraint Types

### Performance Constraints
- Response time limits
- Throughput requirements
- Memory usage limits
- CPU utilization caps

### Physical Constraints
- Size and weight limits
- Environmental conditions
- Durability requirements
- Power consumption limits

### Regulatory Constraints
- Safety standards compliance
- Security requirements
- Accessibility standards
- Industry regulations

### Design Constraints
- Technology stack limitations
- Integration requirements
- Backward compatibility
- User interface standards

## Constraint Documentation

### In Requirements Files
```
Name: WebServerResponse
Description: Web server must respond quickly to user requests
Constraints: MaxResponseTime2sec
Type: requirement
Status: not done
```

### In Constraint Files
```
Name: MaxResponseTime2sec
Description: Maximum response time of 2 seconds for web requests
Measurement: Response time from request to first byte
Verification: Automated load testing
Units: seconds
Threshold: 2.0
```

## Troubleshooting Constraint Issues

### Conflict Resolution
1. **Identify the conflict**: Use rmToo's analysis tools
2. **Analyze the hierarchy**: Understand constraint inheritance
3. **Resolve at appropriate level**: Modify constraints or requirements
4. **Verify the solution**: Check that all constraints are satisfied

### Common Problems
- **Over-constraining**: Too many restrictive constraints
- **Under-constraining**: Missing important limitations
- **Inheritance issues**: Unexpected constraint propagation
- **Measurement problems**: Unclear or unmeasurable constraints

## Integration with Quality Analytics

rmToo's analytics modules can help with constraint management:
- **Constraint coverage analysis**: Ensure all requirements have appropriate constraints
- **Conflict detection**: Identify contradictory constraints
- **Compliance tracking**: Monitor constraint satisfaction
- **Impact analysis**: Understand constraint change effects

## See Also

- [Requirements Format](format.md) - How to write requirements with constraints
- [Dependencies](dependencies.md) - How constraint inheritance works
- [Quality Analytics](../analytics/overview.md) - Tools for constraint analysis
- [Testing Guide](../../developer-guide/testing.md) - Constraint verification approaches