from pydantic import BaseModel, Field
from langchain.tools import tool


class CalculationInput(BaseModel):
    """Input schema for CalculationInput."""
    operation: str = Field(...,description="The mathematical operation to perform")
    factor: float = Field(..., description="A factor by which to multiply the result of the operation")

    @tool("perform_calculation", args_schema = CalculationInput, return_direct = True)
    def perform_calculation(operation: str, factor: float) -> str:
        """
        Performs a specified mathematical operation and multiplies the result by a factor.
        
        Parameters:
        - operation (str): A string representing the mathematical operation
        - factor (float): A factor by which to multiply the result or the operation.

        Returns:
        - A string representation of the calculation result.
        """

        # Perform the calculation
        result = eval(operation) * factor